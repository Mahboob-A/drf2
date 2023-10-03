# Generated by Django 4.2.2 on 2023-10-03 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(max_length=30)),
                ('album_name', models.CharField(max_length=30)),
                ('total_songs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=3)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='api.album')),
            ],
        ),
    ]
