from faker import Factory

from oddaj_w_dobre_rece_app.models import User


def create_user():
    fake = Factory.create("pl_PL")
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    return password, last_name, first_name, email


def create_users():
    for user in range(0, 30):
        last_name, first_name, email, password = create_user()
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
        )





