# Generated by Django 4.2.2 on 2024-04-11 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_stocktransaction_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='phonebrand',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='core.serviceproduct'),
        ),
        migrations.AddField(
            model_name='phonemodal',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modals', to='core.serviceproduct'),
        ),
    ]
