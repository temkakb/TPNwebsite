# Generated by Django 3.1.4 on 2021-01-02 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='mausac',
        ),
    ]
