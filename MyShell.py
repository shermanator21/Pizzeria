import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizza.models import Pizza, Topping

pizzas = Pizza.objects.all()

for pizza in pizza:
    print(pizza.id, pizza)

toppings = t.topping_set.all()

for topping in toppings:
    print(topping)