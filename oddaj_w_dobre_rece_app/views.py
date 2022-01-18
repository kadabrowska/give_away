from django.db.models import Count, Sum
from django.shortcuts import render
from django.views import View

from oddaj_w_dobre_rece_app.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        quantity_donated = Donation.objects.annotate(Sum('quantity'))
        institutions_supported = Institution.objects.count()
        ctx = {'quantity_donated': quantity_donated,
               'institutions_supported': institutions_supported}
        return render(request, "index.html", ctx)


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")