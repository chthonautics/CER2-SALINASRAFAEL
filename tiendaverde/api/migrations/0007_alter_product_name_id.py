# Generated by Django 5.1.2 on 2024-10-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_product_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name_id',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
