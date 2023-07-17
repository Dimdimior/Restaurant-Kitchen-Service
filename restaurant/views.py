from django.shortcuts import render
from django.views import generic

from restaurant.models import Dish, DishType, Cook


# Create your views here.


def index(request):
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_cooks": num_cooks,
    }
    return render(request, "restaurant/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 10


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class CookDetailView(generic.DetailView):
    model = Cook
