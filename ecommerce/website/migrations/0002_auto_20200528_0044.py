# Generated by Django 3.0.6 on 2020-05-27 19:14

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('MW', 'Mens Wear'), ('WW', 'Womens Wear'), ('EC', 'Electronics'), ('FW', 'Foot Wear')], default='MW', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('N', ''), ('P', 'popular'), ('S', 'sale')], default='N', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=django_mysql.models.ListCharField(models.CharField(max_length=15), default=['new'], max_length=160, size=10),
            preserve_default=False,
        ),
    ]
