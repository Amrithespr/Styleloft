# Generated by Django 4.2 on 2023-08-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0005_alter_femaleshop2_phone_alter_femaleshop3_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewFemaleShop1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('review', models.CharField(max_length=250)),
            ],
        ),
    ]
