import json

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
def webhook(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    return JsonResponse({"status": "error"})




