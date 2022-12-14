# Generated by Django 4.1.3 on 2022-11-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('dress_type', models.CharField(max_length=20)),
                ('shoulder_to_shoulder', models.CharField(max_length=20)),
                ('above_bust', models.CharField(max_length=20)),
                ('top_bust', models.CharField(max_length=20)),
                ('below_bust', models.CharField(max_length=20)),
                ('blouse_length', models.CharField(max_length=20)),
                ('arm_hole', models.CharField(max_length=20)),
                ('arm_width', models.CharField(max_length=20)),
                ('arm_length', models.CharField(max_length=20)),
                ('waist', models.CharField(max_length=20)),
                ('saree_length', models.CharField(max_length=20)),
                ('saree_waist', models.CharField(max_length=20)),
                ('knee_to_knee', models.CharField(max_length=20)),
                ('thavani', models.CharField(max_length=20)),
                ('pyjama_waist', models.CharField(max_length=20)),
                ('pyjama_hip', models.CharField(max_length=20)),
                ('pyjama_length', models.CharField(max_length=20)),
                ('pyjama_ankle', models.CharField(max_length=20)),
            ],
        ),
    ]
