# Generated by Django 4.2.3 on 2023-07-20 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0079_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='note',
        ),
        migrations.RemoveField(
            model_name='note',
            name='music',
        ),
    ]
