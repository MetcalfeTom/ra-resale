# Generated by Django 2.1.4 on 2018-12-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resale_active',
            field=models.BooleanField(default=False),
        ),
    ]