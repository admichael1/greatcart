# Generated by Django 3.1 on 2023-06-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20230613_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='body',
        ),
    ]
