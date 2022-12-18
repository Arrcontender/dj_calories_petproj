# Generated by Django 4.1.3 on 2022-12-18 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_calculator_date_alter_calculator_total_calories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDataChanges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_weight', models.DecimalField(decimal_places=1, max_digits=15)),
                ('body_height', models.DecimalField(decimal_places=1, max_digits=15)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]