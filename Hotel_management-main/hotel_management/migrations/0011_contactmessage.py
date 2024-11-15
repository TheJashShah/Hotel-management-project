# Generated by Django 4.2.4 on 2023-11-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_management', '0010_images_remove_roomimage_room_remove_roomrating_room_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
