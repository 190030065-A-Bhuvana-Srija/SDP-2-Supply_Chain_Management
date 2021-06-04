# Generated by Django 3.1.7 on 2021-05-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharewithcare_app', '0013_auto_20210515_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('brand', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='butter/')),
            ],
        ),
        migrations.CreateModel(
            name='CreamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('brand', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='cream/')),
            ],
        ),
        migrations.CreateModel(
            name='CurdModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('brand', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='curd/')),
            ],
        ),
        migrations.CreateModel(
            name='GheeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('brand', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='ghee/')),
            ],
        ),
        migrations.CreateModel(
            name='PaneerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('brand', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='paneer/')),
            ],
        ),
    ]
