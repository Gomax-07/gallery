# Generated by Django 3.2.7 on 2021-09-07 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210906_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=25)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.image')),
            ],
        ),
    ]
