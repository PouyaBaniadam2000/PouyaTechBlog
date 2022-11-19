# Generated by Django 4.1.3 on 2022-11-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('who_are_we', models.TextField(max_length=500)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('subject', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('message', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
