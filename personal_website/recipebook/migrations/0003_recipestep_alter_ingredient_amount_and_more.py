# Generated by Django 4.2.17 on 2024-12-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0002_alter_recipe_recipe_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000, verbose_name='step')),
            ],
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(choices=[('gallon', 'Gallon(s)'), ('g', 'Gram(s)'), ('pint', 'Pint(s)'), ('lbs', 'Pound(s)'), ('mL', 'Milliliter(s)'), ('tsp', 'Teaspoon(s)'), ('tbsp', 'Tablespoon(s)'), ('cup', 'Cup(s)'), ('quart', 'Quart(s)'), ('floz', 'Fluid Ounce(s)')], max_length=200, verbose_name='measurement'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='amt_served',
            field=models.IntegerField(default=1, verbose_name='amount served'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_desc',
            field=models.CharField(max_length=400, verbose_name='recipe description'),
        ),
    ]
