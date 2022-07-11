# Generated by Django 4.0 on 2022-06-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_svg_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('features_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('icon_color', models.CharField(blank=True, max_length=254, null=True)),
                ('icon_class', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]