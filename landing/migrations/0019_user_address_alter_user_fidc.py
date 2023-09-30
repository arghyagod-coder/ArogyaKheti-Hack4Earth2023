# Generated by Django 4.2.5 on 2023-09-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_alter_user_fidc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, max_length=700),
        ),
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=118562115620583690929851326209827731232, unique=True),
        ),
    ]