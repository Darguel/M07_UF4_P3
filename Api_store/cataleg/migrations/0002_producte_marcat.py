# Generated by Django 4.2.13 on 2024-05-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cataleg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producte',
            name='marcat',
            field=models.BooleanField(default=True),
        ),
    ]
