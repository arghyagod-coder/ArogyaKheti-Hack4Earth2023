# Generated by Django 4.2.5 on 2023-09-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0027_alter_user_fidc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=269732325640682250650484223775784042219, unique=True),
        ),
    ]
