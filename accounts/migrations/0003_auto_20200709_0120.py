# Generated by Django 3.0.7 on 2020-07-09 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Furniture&Decoration', 'Furniture&Decoration'), ('Beauty&Fashion', 'Beauty&Fashion'), ('Appliances&Split', 'Appliances&Split'), ('Imported&Utilities', 'Imported&Utilities'), ('Games,Movies&Books', 'Games,Movies&Books'), ('Fitness&Health', 'Fitness&Health'), ('Innovations', 'Innovations'), ('Others', 'Others')], max_length=100, null=True),
        ),
    ]
