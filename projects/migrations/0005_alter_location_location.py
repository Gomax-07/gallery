# Generated by Django 3.2.7 on 2021-09-07 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=150),
        ),
    ]
