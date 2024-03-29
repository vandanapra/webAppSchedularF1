# Generated by Django 3.2.12 on 2022-04-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='machineDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=122)),
                ('Manufacturer', models.CharField(max_length=122)),
                ('shopName', models.CharField(max_length=122)),
                ('MachineNo', models.CharField(max_length=122)),
                ('Description', models.CharField(default=0, max_length=122)),
                ('remarks', models.CharField(default=0, max_length=122)),
                ('currentDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='productionOrder',
            fields=[
                ('sno', models.IntegerField(primary_key=b'I01\n', serialize=False)),
                ('orderRefNo', models.CharField(max_length=122)),
                ('orderVariant', models.CharField(max_length=122)),
                ('orderStartDate', models.DateField(null=True)),
                ('orderEndDate', models.DateField(null=True)),
                ('orderQuantity', models.CharField(max_length=122)),
                ('orderPriority', models.CharField(max_length=122)),
                ('currentDate', models.DateField()),
            ],
        ),
    ]
