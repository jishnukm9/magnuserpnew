# Generated by Django 4.2.8 on 2024-06-21 11:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_livestreamurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='createddate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livestreamurl',
            name='url',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
