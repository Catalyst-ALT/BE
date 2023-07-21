# Generated by Django 4.2.3 on 2023-07-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0083_upload_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movement',
            name='user',
        ),
        migrations.AddField(
            model_name='movement',
            name='note',
            field=models.TextField(default='take notes'),
        ),
        migrations.AddField(
            model_name='upload',
            name='text',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='music',
            name='note',
            field=models.TextField(default='take notes'),
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]