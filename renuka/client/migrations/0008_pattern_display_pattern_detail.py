# Generated by Django 4.1.3 on 2022-12-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_ornaments_display_ornaments_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern_display',
            name='pattern_detail',
            field=models.CharField(default='details here', max_length=200),
        ),
    ]
