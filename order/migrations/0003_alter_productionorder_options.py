# Generated by Django 5.0.3 on 2024-03-12 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_productionorder_id_productionorder_orderid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productionorder',
            options={'verbose_name': 'Sales Order', 'verbose_name_plural': 'Sales Orders'},
        ),
    ]