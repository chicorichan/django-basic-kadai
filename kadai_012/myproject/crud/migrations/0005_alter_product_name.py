# Generated by Django 5.0.3 on 2024-03-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
