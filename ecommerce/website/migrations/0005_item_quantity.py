# Generated by Django 3.0.6 on 2020-05-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
