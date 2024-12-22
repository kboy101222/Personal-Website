from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Ingredient
from .models import Recipe
from .models import RecipeStep


class IngredientsInline(admin.TabularInline):
    model = Ingredient
    extra = 2


class RecipeStepsInline(admin.TabularInline):
    model = RecipeStep
    extra = 2
    formfields_overrides = {
        models.CharField: {"widget": Textarea()},
    }


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Recipe Info",
            {
                "fields": [
                    "recipe_name",
                    "recipe_type",
                    "date_added",
                    "recipe_desc",
                    "amt_served",
                    "recipe_img",
                ],
            },
        ),
    ]
    inlines = [IngredientsInline, RecipeStepsInline]


# Register your models here.
