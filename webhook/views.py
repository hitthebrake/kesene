import json

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render


# Create your views here.
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


def child_path1(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path2(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path3(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path4(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path5(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path6(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path7(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path8(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path9(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path10(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path11(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path12(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path13(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path14(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path15(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path16(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path17(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path18(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path19(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path20(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path21(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path22(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path23(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path24(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path25(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path26(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path27(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path28(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path29(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path30(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path31(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path32(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path33(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path34(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path35(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path36(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path37(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path38(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path39(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path40(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path41(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path42(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path43(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path44(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path45(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path46(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path47(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path48(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path49(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path50(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path51(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path52(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path53(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path54(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path55(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path56(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path57(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path58(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path59(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path60(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path61(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path62(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path63(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path64(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path65(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path66(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path67(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path68(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path69(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path70(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path71(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path72(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path73(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path74(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path75(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path76(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path77(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path78(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path79(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path80(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path81(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path82(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path83(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path84(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path85(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path86(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path87(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path88(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path89(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path90(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path91(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path92(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path93(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path94(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path95(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path96(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path97(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path98(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path99(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path100(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path101(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path102(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path103(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path104(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path105(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path106(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path107(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path108(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path109(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path110(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path111(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path112(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path113(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path114(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path115(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path116(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path117(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path118(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path119(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")


def child_path120(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST with JSON is allowed")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return JsonResponse({"status": "success"})
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")




