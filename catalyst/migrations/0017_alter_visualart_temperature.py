# Generated by Django 4.2.3 on 2023-07-17 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0016_alter_visualart_emotion_alter_visualart_sentiment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualart',
            name='temperature',
            field=models.DecimalField(decimal_places=1, default=0.8, max_digits=2),
        ),
    ]