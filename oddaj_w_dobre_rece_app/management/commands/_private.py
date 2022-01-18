from faker import Factory

from oddaj_w_dobre_rece_app.models import User


def create_user():
    fake = Factory.create("pl_PL")
    password = fake.password()
    last_login = fake.date_this_month(before_today=True, after_today=False)
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = fake.user_name()
    email = fake.email()
    is_staff = False
    is_superuser = False
    is_active = True
    date_joined = fake.date_this_month(before_today=True, after_today=False)
    return password, last_login, last_name, first_name, username, is_superuser, email, is_staff, is_active, date_joined


def create_users():
    for user in range(0, 30):
        password, last_login, last_name, first_name, username, is_superuser, email, is_staff, is_active, date_joined = create_user()
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            password=password,
            last_login=last_login,
            username=username,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            email=email,
            date_joined=date_joined,
        )





