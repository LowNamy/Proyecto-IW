# Generated by Django 4.1.2 on 2022-11-29 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_fecha_disco_lanzamiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistas',
            name='imagenArtista',
            field=models.ImageField(null=True, upload_to='artistas'),
        ),
    ]
