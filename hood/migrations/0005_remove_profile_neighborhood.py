# Generated by Django 3.2.9 on 2021-12-26 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_hoodmember'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='neighborhood',
        ),
    ]
