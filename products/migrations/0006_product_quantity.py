# Generated by Django 5.0.3 on 2024-03-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
    ]