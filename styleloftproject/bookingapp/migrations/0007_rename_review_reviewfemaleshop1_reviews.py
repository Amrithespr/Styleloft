# Generated by Django 4.2 on 2023-08-06 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0006_reviewfemaleshop1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewfemaleshop1',
            old_name='review',
            new_name='reviews',
        ),
    ]
