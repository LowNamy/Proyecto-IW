# Generated by Django 4.1.2 on 2022-11-28 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disco',
            name='imDisco',
        ),
    ]
