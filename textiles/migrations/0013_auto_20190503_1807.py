# Generated by Django 2.1.3 on 2019-05-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textiles', '0012_auto_20181224_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
