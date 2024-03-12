# Generated by Django 5.0.3 on 2024-03-12 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inhouseinventory_description'),
        ('products', '0006_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roq_minimum_quantity', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('roq_maximum_quantity', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('roq_minimum_period_of_cover', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('roq_maximum_period_of_cover', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('safety_stock_minimum_quantity', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('safety_stock_maximum_quantity', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('safety_stock_minimum_period_of_cover', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('safety_stock_maximum_period_of_cover', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('service_level', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('lead_time', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('lead_time_deviation', models.CharField(blank=True, max_length=50, null=True, verbose_name='')),
                ('donot_stock', models.BooleanField(default=False)),
                ('current_available', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.DeleteModel(
            name='inhouseInventory',
        ),
        migrations.AddField(
            model_name='inventory',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.location', verbose_name=''),
        ),
    ]
