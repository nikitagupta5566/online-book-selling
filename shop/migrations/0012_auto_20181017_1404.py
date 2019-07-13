# Generated by Django 2.0.7 on 2018-10-17 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20181016_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Cart'),
        ),
    ]
