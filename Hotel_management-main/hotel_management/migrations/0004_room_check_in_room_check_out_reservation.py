# Generated by Django 4.2.4 on 2023-11-03 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_management', '0003_rename_rooms_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='check_in',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='check_out',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_management.room')),
            ],
        ),
    ]
