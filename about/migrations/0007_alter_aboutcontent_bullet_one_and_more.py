# Generated by Django 4.0 on 2022-07-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontent',
            name='bullet_one',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='aboutcontent',
            name='bullet_three',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='aboutcontent',
            name='bullet_two',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
