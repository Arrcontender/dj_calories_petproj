# Generated by Django 4.1.3 on 2022-12-04 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_remove_calculator_product_remove_calculator_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.products'),
        ),
        migrations.AddField(
            model_name='calculator',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
