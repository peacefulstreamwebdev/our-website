# Generated by Django 4.0 on 2022-07-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('title', models.CharField(max_length=254)),
                ('blurb', models.TextField(max_length=1000)),
            ],
        ),
    ]