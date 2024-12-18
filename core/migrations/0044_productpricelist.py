# Generated by Django 4.2.8 on 2024-06-10 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0043_alter_branchpurchase_invoicenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('modal', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('price1', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productpricelist', to=settings.AUTH_USER_MODEL)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productpricelist', to='core.branch')),
            ],
        ),
    ]
