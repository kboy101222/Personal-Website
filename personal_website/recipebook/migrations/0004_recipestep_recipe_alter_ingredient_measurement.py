# Generated by Django 4.2.17 on 2024-12-20 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0003_recipestep_alter_ingredient_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipestep',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='recipebook.recipe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(choices=[('lbs', 'Pound(s)'), ('pint', 'Pint(s)'), ('tbsp', 'Tablespoon(s)'), ('floz', 'Fluid Ounce(s)'), ('mL', 'Milliliter(s)'), ('quart', 'Quart(s)'), ('cup', 'Cup(s)'), ('tsp', 'Teaspoon(s)'), ('gallon', 'Gallon(s)'), ('g', 'Gram(s)')], max_length=200, verbose_name='measurement'),
        ),
    ]
