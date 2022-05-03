# Generated by Django 3.2.11 on 2022-04-28 15:47
import json
from django.db import migrations
from django.db import transaction


def add_ingridients(apps, schema_editor):
    Ingredient = apps.get_model('recipes', 'Ingredient')
    json_file_path = ('../data/ingredients.json')

    with open(json_file_path, encoding='utf-8') as f:
        data = json.load(f)

        with transaction.atomic():
            for item in data:
                ingredient = Ingredient.objects.get_or_create(
                    name=item['name'],
                    measurement_unit=item['measurement_unit']
                )


class Migration(migrations.Migration):
    dependencies = [
        ('recipes', '0002_delete_ingredientquantity'),
    ]

    operations = [
        migrations.RunPython(add_ingridients),
    ]
