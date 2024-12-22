from django.urls import path

from . import views

app_name = "recipebook"
urlpatterns = [
    # index
    path("", views.index, name="index"),
    # recipe list
    path("recipe_list/", views.recipe_list, name="recipe_list"),
    # specific recipe
    path("recipe_list/<int:recipe_id>", views.recipe, name="recipe"),
    # filtered recipe list
    path("recipe_list/filter", views.filtered_recipe_list, name="filtered_recipe_list"),
    # testing a new filtered recipe list
    # path("recipe_list/<str:recipe_type>", views.filtered_recipe_list, name="filtered_recipe_list")
]
