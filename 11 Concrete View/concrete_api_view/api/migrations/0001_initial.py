# Generated by Django 4.2.2 on 2023-08-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('money', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
