# Generated by Django 4.0 on 2022-08-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]