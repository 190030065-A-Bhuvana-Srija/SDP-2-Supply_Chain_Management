# Generated by Django 3.1.5 on 2021-01-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20210129_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='photo',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]
