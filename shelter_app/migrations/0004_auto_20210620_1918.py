# Generated by Django 3.1.7 on 2021-06-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_app', '0003_auto_20210618_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='photo_height',
            field=models.PositiveIntegerField(default=300),
        ),
        migrations.AddField(
            model_name='pet',
            name='photo_width',
            field=models.PositiveIntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, height_field='photo_height', upload_to='pets_photo', width_field='photo_width'),
        ),
    ]