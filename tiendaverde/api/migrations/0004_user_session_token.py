# Generated by Django 5.1.2 on 2024-10-20 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='session_token',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
