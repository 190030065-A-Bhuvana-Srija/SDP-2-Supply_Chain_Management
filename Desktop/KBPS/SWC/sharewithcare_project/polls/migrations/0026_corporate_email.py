# Generated by Django 3.1.5 on 2021-03-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='corporate',
            name='email',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
