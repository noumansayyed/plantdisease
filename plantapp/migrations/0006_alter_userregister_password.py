# Generated by Django 4.2.8 on 2023-12-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantapp', '0005_rename_user_userregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]