# Generated by Django 4.2.5 on 2023-09-26 10:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_auto_20230926_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="fidc",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
