# Generated by Django 3.2.12 on 2022-04-09 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productionSchedualar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='componentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componet_name', models.CharField(max_length=122)),
                ('DrawingNo', models.CharField(max_length=122)),
                ('qpp', models.CharField(max_length=122)),
                ('Level', models.CharField(max_length=122)),
                ('description', models.CharField(default=0, max_length=122)),
                ('modelName', models.CharField(default=0, max_length=122)),
                ('currentDate', models.DateField()),
            ],
        ),
    ]
