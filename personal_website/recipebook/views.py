from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Ingredient
from .models import Recipe, RecipeStep

from .helper import RECIPE_TYPES

# Create your views here.
def index(request):
    return render(request, template_name="recipebook/index.html")


def recipe_list(request):
    recipes = Recipe.objects.order_by("recipe_name")

    return render(
        request,
        template_name="recipebook/recipe_list.html",
        context={"recipe_list": recipes, "recipe_types":RECIPE_TYPES},
    )

def filtered_recipe_list(request):
    recipe_type = request.POST["type-selection"]
    if recipe_type != "all" and recipe_type != "not_set":
        recipes = Recipe.objects.filter(recipe_type__exact=recipe_type).order_by("recipe_name")
    else:
        recipes = recipes = Recipe.objects.order_by("recipe_name")

    return render(
        request,
        template_name="recipebook/recipe_list.html",
        context={"recipe_list": recipes, "recipe_types":RECIPE_TYPES},
    )
    
def recipe(request, recipe_id):
    recipe_info = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = Ingredient.objects.filter(recipe__exact=recipe_id)
    recipe_steps = RecipeStep.objects.filter(recipe__exact=recipe_id)
    return render(
        request,
        template_name="recipebook/recipe.html",
        context={"recipe_info": recipe_info, "ingredients": ingredients, "recipe_steps": recipe_steps},
    )
