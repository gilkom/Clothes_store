# Generated by Django 3.2.11 on 2022-01-06 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.manufacturer'),
        ),
    ]