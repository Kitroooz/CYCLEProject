# Generated by Django 4.2.4 on 2023-08-30 21:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default=True, max_length=30)),
                ('Surname', models.CharField(blank=True, default=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='static/')),
                ('name', models.CharField(blank=True, default=True, max_length=30)),
                ('manufacturer', models.CharField(default=True, max_length=30)),
                ('description', models.TextField(default=True, max_length=1000)),
                ('price', models.IntegerField(default=True)),
                ('stock', models.IntegerField(default=True)),
                ('type', models.CharField(blank=True, default=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, default=True, max_length=30)),
                ('Surname', models.CharField(blank=True, default=True, max_length=30)),
            ],
        ),
    ]
