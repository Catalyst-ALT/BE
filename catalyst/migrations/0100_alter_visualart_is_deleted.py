# Generated by Django 4.2.3 on 2023-07-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0099_visualart_is_deleted_delete_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualart',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
