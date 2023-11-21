# Generated by Django 4.2 on 2023-06-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0002_rename_femaleservices_femaleservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='femaleshop1',
            name='phone',
            field=models.IntegerField(default=0.0008250825082508251, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='femaleshop2',
            name='phone',
            field=models.IntegerField(default=0.08333333333333333, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='femaleshop3',
            name='phone',
            field=models.IntegerField(default=0.0008250825082508251, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='femaleshop4',
            name='phone',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maleshop1',
            name='phone',
            field=models.IntegerField(default=7.992327365728901e-05, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maleshop2',
            name='phone',
            field=models.IntegerField(default=0.000819000819000819, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maleshop3',
            name='phone',
            field=models.IntegerField(default=0.0008250825082508251, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maleshop4',
            name='phone',
            field=models.IntegerField(default=0.0008250825082508251, max_length=10),
            preserve_default=False,
        ),
    ]