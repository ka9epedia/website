# Generated by Django 2.1.4 on 2018-12-07 06:25

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20181203_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='summary',
            field=martor.models.MartorField(),
        ),
    ]