# Generated by Django 3.2.1 on 2021-05-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rating', '0004_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]