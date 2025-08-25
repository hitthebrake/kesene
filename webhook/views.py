import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.

@login_required(login_url='authorization:login')
def webhook(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    return JsonResponse({"status": "error"})




