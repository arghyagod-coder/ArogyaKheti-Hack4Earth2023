# Generated by Django 4.2.5 on 2023-09-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produce',
            name='farmerid',
            field=models.IntegerField(blank=True),
        ),
    ]