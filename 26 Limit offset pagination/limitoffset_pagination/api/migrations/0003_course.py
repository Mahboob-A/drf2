# Generated by Django 4.2.2 on 2023-09-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_album_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('student', models.ManyToManyField(related_name='course', to='api.student')),
            ],
        ),
    ]