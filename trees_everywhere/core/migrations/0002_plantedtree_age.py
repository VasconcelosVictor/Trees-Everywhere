# Generated by Django 5.0.6 on 2024-06-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantedtree',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
