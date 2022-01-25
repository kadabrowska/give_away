from django.db.models import Sum
from django.shortcuts import render
from django.views import View

from oddaj_w_dobre_rece_app.models import Donation, Institution

from django.conf import settings
User = settings.AUTH_USER_MODEL


class LandingPageView(View):
    def get(self, request):
        quantity_donated = Donation.objects.all().aggregate(total=Sum('quantity')).get('total')
        institutions_supported = Donation.objects.count()
        foundation_list = Institution.objects.filter(type="FUNDACJA")
        organisation_list = Institution.objects.filter(type="ORGANIZACJA POZARZĄDOWA")
        local_collection_list = Institution.objects.filter(type="ZBIÓRKA LOKALNA")
        ctx = {'quantity_donated': quantity_donated,
               'institutions_supported': institutions_supported,
               'foundation_list': foundation_list,
               'organisation_list': organisation_list,
               'local_collection_list': local_collection_list}
        return render(request, "index.html", ctx)


class AddDonationView(View):
    def get(self, request):
        return render(request, "form.html")
