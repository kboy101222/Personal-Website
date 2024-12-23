from django import template
from math import floor

register = template.Library()

measurement_formatting = {
    "tsp": "teaspoon",
    "tbsp": "tablespoon",
    "floz": "fluid ounce",
    "cup": "cup",
    "pint": "pint",
    "quart": "quart",
    "gallon": "gallon",
    "lbs": "pound",
    "g": "gram",
    "mL": "milliliter",
    "amt": "",
    "stick": "stick",
    "not_set": "",
    "fluid ounce": "fluid ounce",
    "tablespoon" : "tablespoon",
    "pound" : "pound",
    "gram" : "gram",
    "milliliter" : "milliliter",
}

def checkPlural(amount, measure="not_set"):
    if measure == "":
        if amount > 1 or amount == 0:
            return str(int(amount)) + " "
        return str(int(amount))
    else:
        if amount > 1 or amount == 0:
            return str(int(amount)) + " " + measurement_formatting[measure] + "s"
        return str(int(amount))


@register.filter
def format(value):
    value = value.replace("_", " ")
    return value.title()


@register.filter
def measurement(value, arg):
    # arg is the amount so plurals can be formatted
    
    if arg.is_integer():
        return checkPlural(arg, measurement_formatting[value])
    
    amt_fraction = arg.as_integer_ratio()
    whole_num = int(floor(amt_fraction[0] / amt_fraction[1]))
    if whole_num == 0:
        return str(amt_fraction[0]) + "/" + str(amt_fraction[1]) + " " + measurement_formatting[value]
    else:
        numer = amt_fraction[0] - (whole_num * amt_fraction[1])
        whole_num = str(whole_num) + " "
        return whole_num + " " + str(numer) + "/" + str(amt_fraction[1]) + " " + measurement_formatting[value] + "s"


@register.filter
def nospaces(value):
    return value.replace(" ", "_")
