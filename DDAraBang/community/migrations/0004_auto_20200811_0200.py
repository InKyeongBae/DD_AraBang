# Generated by Django 2.2.15 on 2020-08-11 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_post_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(blank=True, choices=[('한양대학교', '한양대학교'), ('경희대학교', '경희대학교'), ('중양대학교', '중양대학교'), ('연세대학교', '연세대학교')], max_length=30),
        ),
    ]