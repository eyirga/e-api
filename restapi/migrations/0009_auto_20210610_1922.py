# Generated by Django 3.1.7 on 2021-06-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0008_auto_20210607_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='name',
            new_name='category_name',
        ),
        migrations.AlterField(
            model_name='albumlist',
            name='created',
            field=models.DateField(default='2021-06-10'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created',
            field=models.DateField(default='2021-06-10'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='due_date',
            field=models.DateField(default='2021-06-10'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='scheduled_date',
            field=models.DateField(default='2021-06-10'),
        ),
    ]