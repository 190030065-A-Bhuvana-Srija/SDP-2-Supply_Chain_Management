# Generated by Django 3.1.5 on 2021-01-28 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20210128_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='photo',
            field=models.ImageField(default=0, upload_to='image'),
        ),
    ]