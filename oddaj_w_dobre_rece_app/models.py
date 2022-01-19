from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


INSTITUTIONS = (
    ('FUNDACJA', 'fundacja'),
    ('ORGANIZACJA POZARZĄDOWA', 'organizacja pozarządowa'),
    ('ZBIÓRKA LOKALNA', 'zbiórka lokalna'),
)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length= 35, choices=INSTITUTIONS, default='FUNDACJA')
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=8)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


# class User(AbstractUser):
#
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'email'


