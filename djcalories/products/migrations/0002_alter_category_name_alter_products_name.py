# Generated by Django 4.1.3 on 2022-11-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]