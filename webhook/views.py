import json

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

from webhook.models import WebhookRequest


# Create your views here.
def webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            WebhookRequest.objects.create(
                data=data,
            )

            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")

    return HttpResponseBadRequest("Only POST with JSON is allowed")

def ashana_vent_shaft_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_slope_vault_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_external_wall_H(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_vent_shaft_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_external_wall_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_slope_vault_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_slope_vault_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_external_wall_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def ashana_external_wall_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_big_vent_shaft_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_big_slope_vault_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_big_vent_shaft_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_big_slope_vault_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_big_slope_vault_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def enter1_window_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def enter1_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def enter2_window_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def enter2_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def gurhana_door_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def gurhana_window_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def gurhana_door_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def gurhana_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def gurhana_window_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_door_IO(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_north_east_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_north_west_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_south_east_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_south_west_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_south_west_window_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_north_east_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_north_west_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_south_east_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_south_west_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_south_west_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_vertex_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_vertex_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_out_5_H(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_out_5_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_out_H(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_out_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_in_H(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_in_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_center_5_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_center_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_out_5_H(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_out_5_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_out_H(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_out_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_in_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_in_H(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_center_5_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_center_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_north_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_south_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_east_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qazandyq_dome_west_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def library_vent_shaft_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def library_vent_shaft_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hall2_west_door_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hall2_west_door_IO(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hall2_west_door_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hall4_25_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hall4_25_CO2(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hall4_25_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_vent_shaft_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_slope_vault_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_window_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_window_IO(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_vent_shaft_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_slope_vault_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_slope_vault_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def qydyqhana_wall_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_small_vent_shaft_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_small_slope_vault_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_small_vent_shaft_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_small_vent_shaft_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_small_slope_vault_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def aqsaray_small_slope_vault_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def room_window_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def room_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def room_window_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def terrace_window_V(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def terrace_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def terrace_window_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hudjara_window_T(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def hudjara_window_t(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def others_north_corner_noise(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def others_east_corner_slope(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def others_north_corner_slope(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def others_west_corner_slope(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def others_south_corner_slope(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def others_well_water_level(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def meteodata_meteodata(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")






