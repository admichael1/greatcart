# Generated by Django 3.1 on 2023-06-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_contact_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='body',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
