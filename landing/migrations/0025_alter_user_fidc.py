# Generated by Django 4.2.5 on 2023-09-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0024_alter_user_fidc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=268277487421129767379867272498728973551, unique=True),
        ),
    ]
