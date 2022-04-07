# Generated by Django 3.1.4 on 2022-04-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20220407_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='duration',
            field=models.CharField(default='empty', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='main_features',
            field=models.TextField(default='Empty'),
        ),
        migrations.AlterField(
            model_name='project',
            name='video_url',
            field=models.CharField(max_length=500),
        ),
    ]
