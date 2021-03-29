# Generated by Django 2.1.3 on 2018-11-20 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textiles', '0003_auto_20181119_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_product_name', models.CharField(max_length=500)),
                ('material', models.CharField(max_length=100)),
                ('length', models.DecimalField(decimal_places=4, max_digits=5)),
                ('color', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_product', to='textiles.Product')),
            ],
        ),
        migrations.AddField(
            model_name='productimage',
            name='label',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]