# Generated by Django 4.1.4 on 2023-05-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
    ]