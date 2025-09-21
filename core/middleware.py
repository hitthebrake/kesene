from django.shortcuts import redirect
from django.contrib.auth import logout

class UserValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        if user.is_authenticated:
            if not user.is_active or getattr(user, "is_deleted", False):
                logout(request)
                return redirect("authorization:login")

        return self.get_response(request)