# Generated by Django 3.1.7 on 2021-06-11 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_auto_20210610_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albumcategory',
            old_name='name',
            new_name='album_category',
        ),
        migrations.RenameField(
            model_name='blogcategory',
            old_name='name',
            new_name='blog_category',
        ),
        migrations.RenameField(
            model_name='bookcategory',
            old_name='name',
            new_name='book_category',
        ),
        migrations.RenameField(
            model_name='clientcategory',
            old_name='name',
            new_name='client_name',
        ),
        migrations.RenameField(
            model_name='contactcategory',
            old_name='name',
            new_name='contact_category',
        ),
        migrations.RenameField(
            model_name='customercategory',
            old_name='name',
            new_name='customer_category',
        ),
        migrations.RenameField(
            model_name='employeecategory',
            old_name='name',
            new_name='employee_category',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customerId',
            new_name='catname',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='orderMasterId',
            new_name='catname',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='title',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='taskcategory',
            old_name='name',
            new_name='task_category',
        ),
        migrations.RenameField(
            model_name='tutorialcategory',
            old_name='name',
            new_name='tutorial_category',
        ),
        migrations.AlterField(
            model_name='albumlist',
            name='created',
            field=models.DateField(default='2021-06-11'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='created',
            field=models.DateField(default='2021-06-11'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='due_date',
            field=models.DateField(default='2021-06-11'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='scheduled_date',
            field=models.DateField(default='2021-06-11'),
        ),
    ]
