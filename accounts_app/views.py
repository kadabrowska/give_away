from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


class LogoutView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
