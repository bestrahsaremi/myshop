# Generated by Django 2.1.5 on 2019-01-17 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='products')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 12, 16, 14, 329630))),
            ],
        ),
    ]
