# Generated by Django 3.1.7 on 2021-06-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20210607_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
