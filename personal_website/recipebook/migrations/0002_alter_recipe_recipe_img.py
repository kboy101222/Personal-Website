# Generated by Django 4.2.17 on 2024-12-20 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_img',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images', verbose_name='recipe image'),
        ),
    ]
