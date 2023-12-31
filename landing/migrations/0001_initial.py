# Generated by Django 4.2.5 on 2023-09-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=10)),
                ('pincode', models.IntegerField(max_length=6)),
                ('farmname', models.CharField(max_length=200)),
                ('farmlandmarks', models.CharField(max_length=200)),
                ('farmarea', models.DecimalField(decimal_places=3, max_digits=10000)),
                ('bio', models.TextField(blank=True, max_length=700)),
            ],
        ),
    ]
