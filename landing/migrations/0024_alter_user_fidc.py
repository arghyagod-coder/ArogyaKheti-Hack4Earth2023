# Generated by Django 4.2.5 on 2023-09-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0023_alter_user_fidc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=143232331814948078505287089740683974321, unique=True),
        ),
    ]
