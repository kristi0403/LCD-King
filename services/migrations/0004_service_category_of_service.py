# Generated by Django 3.2.7 on 2021-10-31 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20211031_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category_of_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.category_of_service'),
        ),
    ]
