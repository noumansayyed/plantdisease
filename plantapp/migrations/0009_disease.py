# Generated by Django 4.2.8 on 2024-01-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantapp', '0008_plantimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageName', models.CharField(max_length=100)),
                ('diseaseName', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
    ]