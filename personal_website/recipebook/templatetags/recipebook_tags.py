from django import template

register = template.Library()


@register.filter
def format(value):
    value = value.replace("_", " ")
    return value.title()


@register.filter
def measurement(value, arg):
    # arg is the amount so plurals can be formatted
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
    }
    amount_fraction = arg.as_integer_ratio()
    whole_num = int(amount_fraction[0]/amount_fraction[1])
    if whole_num >= 1:
        whole_num = str(whole_num) + " "
    else:
        whole_num = ""

    amount = (
        str(amount_fraction[0]) + "/" + str(amount_fraction[1])
        if amount_fraction[1] != 1 and arg > 1
        else str(amount_fraction[0])
    )
    if arg.is_integer():
        return (
            amount
            + " "
            + measurement_formatting[value]
            + ("s" if arg > 1 and arg != 0 and value != "amt" else "")
        )
    else:
        return (
            whole_num
            + " "
            + amount
            + " "
            + measurement_formatting[value]
            + ("s" if arg > 1 and arg != 0 and value != "amt" else "")
        )


@register.filter
def nospaces(value):
    return value.replace(" ", "_")
