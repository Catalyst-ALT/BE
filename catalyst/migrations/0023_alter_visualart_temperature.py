# Generated by Django 4.2.3 on 2023-07-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0022_alter_visualart_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualart',
            name='temperature',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
        ),
    ]
