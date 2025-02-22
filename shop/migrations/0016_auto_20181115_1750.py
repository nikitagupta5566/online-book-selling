# Generated by Django 2.0.7 on 2018-11-15 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20181017_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Description',
            field=models.CharField(max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='book',
            name='Language',
            field=models.CharField(max_length=100, null=True, verbose_name='Language'),
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.IntegerField(blank=True, default=0, verbose_name='Edition'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=500, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='item_image',
            field=models.CharField(max_length=1000, null=True),
        ),
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
