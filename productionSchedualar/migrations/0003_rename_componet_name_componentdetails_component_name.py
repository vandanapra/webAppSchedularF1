# Generated by Django 3.2.12 on 2022-04-09 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productionSchedualar', '0002_componentdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componentdetails',
            old_name='componet_name',
            new_name='component_name',
        ),
    ]
