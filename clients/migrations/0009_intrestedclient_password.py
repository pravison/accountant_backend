# Generated by Django 4.2.6 on 2023-10-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_intrestedclient_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='intrestedclient',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
