# Generated by Django 4.2.5 on 2023-09-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0017_alter_user_fidc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=14388419859092529149126238284078300000, unique=True),
        ),
    ]
