# Generated by Django 2.0.7 on 2018-10-15 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_item_item_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='item',
            new_name='Book',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
