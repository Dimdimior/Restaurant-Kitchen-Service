from django.urls import path, include

from restaurant.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView,
    DishDetailView,
    CookDetailView,
    CookCreateView,
    CookExperienceUpdateView,
    DishCreateView,
    DishUpdateView,
    CookDeleteView,
    DishDeleteView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dishtypes/", DishTypeListView.as_view(), name="dishtypes"),
    path("dishes/", DishListView.as_view(), name="dishes"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update", CookExperienceUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),
    path("dishtypes/create/", DishTypeCreateView.as_view(), name="dishtype-create"),
    path("dishtypes/<int:pk>/update", DishTypeUpdateView.as_view(), name="dishtype-update"),
    path("dishtypes/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dishtype-delete"),
]

app_name = "restaurant"
