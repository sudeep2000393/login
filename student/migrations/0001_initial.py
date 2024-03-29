# Generated by Django 3.2.23 on 2024-01-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
