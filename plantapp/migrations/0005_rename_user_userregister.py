# Generated by Django 4.2.8 on 2023-12-24 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantapp', '0004_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserRegister',
        ),
    ]