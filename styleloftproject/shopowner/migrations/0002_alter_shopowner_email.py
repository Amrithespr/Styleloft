# Generated by Django 4.2 on 2023-06-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopowner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopowner',
            name='email',
            field=models.CharField(max_length=250),
        ),
    ]
