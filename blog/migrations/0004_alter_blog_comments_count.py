# Generated by Django 4.2.4 on 2023-09-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_comments_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='comments_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
