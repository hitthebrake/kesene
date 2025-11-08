import json
import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from django.contrib.admin.views.decorators import staff_member_required

from monitoring.models import TelegramUser
from sensors.models import ScenarioInstance

BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@csrf_exempt
def telegram_webhook(request):
    if request.method != "POST":
        return HttpResponse("OK")

    try:
        update = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponse(status=400)

    # handle messages (text commands)
    message = update.get("message") or update.get("edited_message")
    if not message:
        return HttpResponse("no message")

    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "")

    # store user when they send /start
    if text and text.strip().lower().startswith("/start"):
        TelegramUser.objects.update_or_create(
            chat_id=chat_id,
            defaults={
                "first_name": chat.get("first_name"),
                "username": chat.get("username"),
            },
        )
        # optional: reply to user
        reply_text = "Спасибо, вы успешно зарегистрировались"
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply_text
        })
    # You can handle other commands here

    return HttpResponse("ok")


@staff_member_required
def broadcast_form(request, scenario_id):
    scenario = ScenarioInstance.objects.get(id=scenario_id)
    fixed_text = f'<b>Место установки: </b><i>{scenario.scenario.location}</i>\n<b>Заголовок: </b><i>{scenario.scenario.title}</i>\n<b>Описание: </b>{scenario.scenario.description}'

    users = TelegramUser.objects.all()

    results = []
    for u in users:
        payload = {"chat_id": u.chat_id, "text": fixed_text, "parse_mode": "HTML"}
        try:
            r = requests.post(
                f"{TELEGRAM_API}/sendMessage",
                json=payload,
                timeout=10
            )
            data = r.json()
            if not data.get("ok"):
                err = data.get("description", "")
                if "blocked" in err.lower() or "not found" in err.lower():
                    u.delete()
        except Exception as e:
            results.append((u.chat_id, "error", str(e)))

    messages.success(request, 'Все сообщения отправлены через Telegram бот')

