# Generated by Django 4.2.4 on 2023-10-08 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refferals', '0002_rename_code_refferal_refferal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='refferal',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]