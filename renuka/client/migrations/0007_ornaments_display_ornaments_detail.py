# Generated by Django 4.1.3 on 2022-12-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_rename_ornamnets_image_ornaments_display_ornaments_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ornaments_display',
            name='ornaments_detail',
            field=models.CharField(default='details here', max_length=200),
        ),
    ]
