# Generated by Django 4.1.4 on 2023-02-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_customer_products_remove_product_subcategoryid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='qty',
            field=models.PositiveIntegerField(),
        ),
    ]
