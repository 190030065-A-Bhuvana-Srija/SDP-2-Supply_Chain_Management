# Generated by Django 3.1.5 on 2021-04-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_cart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='photo',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]
