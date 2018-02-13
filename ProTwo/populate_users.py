import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()

from faker import Faker
from AppTwo.models import User
fakegen = Faker()
def populate(N):
    for entry in  range(N):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()

        user = User.objects.get_or_create(first_name = first_name,last_name = last_name,email = email)[0]

if __name__ == "__main__":
    print("Populating Users")
    populate(10)
    print("Populating Complete")
