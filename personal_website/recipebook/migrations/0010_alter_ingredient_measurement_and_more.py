# Generated by Django 5.0.10 on 2024-12-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0009_alter_ingredient_measurement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(choices=[('not_set', 'None'), ('gallon', 'Gallon(s)'), ('quart', 'Quart(s)'), ('g', 'Gram(s)'), ('tsp', 'Teaspoon(s)'), ('tbsp', 'Tablespoon(s)'), ('cup', 'Cup(s)'), ('amt', 'Amount'), ('lbs', 'Pound(s)'), ('mL', 'Milliliter(s)'), ('floz', 'Fluid Ounce(s)'), ('stick', 'Stick'), ('pint', 'Pint(s)')], max_length=200, verbose_name='measurement'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(choices=[('snack', 'Snack'), ('breakfast', 'Breakfast'), ('not_set', 'Not Set'), ('dessert', 'Dessert'), ('lunch', 'Lunch'), ('large_group', 'Large Groups/Parties'), ('holiday', 'Holiday'), ('dinner', 'Dinner')], default='not_set', max_length=20, verbose_name='recipe type'),
        ),
    ]