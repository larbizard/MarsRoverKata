# Generated by Django 3.2.18 on 2023-02-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obstacle',
            name='positionX',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='obstacle',
            name='positionY',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rover',
            name='positionX',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rover',
            name='positionY',
            field=models.IntegerField(),
        ),
    ]
