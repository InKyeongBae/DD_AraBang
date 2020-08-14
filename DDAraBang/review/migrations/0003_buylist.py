# Generated by Django 2.2.3 on 2020-08-14 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_reviewform_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, max_length=100)),
                ('reviewform', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.ReviewForm')),
            ],
        ),
    ]
