# Generated by Django 4.2 on 2023-04-21 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='desctiption',
            new_name='description',
        ),
    ]
