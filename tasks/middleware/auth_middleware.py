from django.shortcuts import redirect
from django.urls import resolve

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resolver_match = request.resolver_match  # This might be None

        if resolver_match and resolver_match.url_name not in ['login', 'register']:  # Check if resolver_match is not None
            if not request.user.is_authenticated:
                return redirect('login')

        response = self.get_response(request)
        return response
