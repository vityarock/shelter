# Generated by Django 3.1.7 on 2021-06-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_app', '0002_auto_20210505_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
    ]
