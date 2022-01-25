from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from django.conf import settings

from accounts_app.models import CustomUser

User = settings.AUTH_USER_MODEL


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        logged_user = authenticate(email=email, password=password)
        if logged_user:
            login(request, logged_user)
            url_next = request.GET.get('next', '/')
            return redirect(url_next)
        else:
            return render(request, 'register.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_2')
        if name and surname and email and password == password_confirmation:
            user = CustomUser.objects.create_user(first_name=name,
                                                  last_name=surname,
                                                  email=email,
                                                  password=password)
            return render(request, 'login.html')
        else:
            return render(request, 'register.html')

