# Generated by Django 5.0.3 on 2024-03-07 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductParentChildRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0, verbose_name='level')),
                ('child_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_item', to='products.product')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_item', to='products.product')),
            ],
            options={
                'verbose_name': 'ProductParentChildRelation',
                'verbose_name_plural': 'ProductParentChildRelations',
            },
        ),
    ]