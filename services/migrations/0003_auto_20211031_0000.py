# Generated by Django 3.2.7 on 2021-10-31 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20211026_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='category_of_service',
        ),
        migrations.AddField(
            model_name='device_of_service',
            name='category_of_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.category_of_service'),
        ),
    ]
