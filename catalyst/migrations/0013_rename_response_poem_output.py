# Generated by Django 4.2.3 on 2023-07-16 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0012_alter_poem_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='response',
            new_name='output',
        ),
    ]
