# Generated by Django 4.2.2 on 2024-08-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_alter_sale_invoicedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktransaction',
            name='reference_number',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='stocktransaction',
            name='transaction_category',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
