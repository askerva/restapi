# Generated by Django 5.0.3 on 2024-03-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=50)),
                ('modelname', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
