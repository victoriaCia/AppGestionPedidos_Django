# Generated by Django 4.0.4 on 2022-05-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='tienda/default.png', upload_to='tienda'),
        ),
    ]
