# Generated by Django 3.1.7 on 2021-06-11 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0011_auto_20210610_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumlist',
            name='album_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapi.taskcategory'),
        ),
    ]
