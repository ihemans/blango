# Generated by Django 3.2.6 on 2023-06-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='value',
        ),
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]
