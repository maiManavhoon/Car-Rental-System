# Generated by Django 4.2.7 on 2024-03-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0016_remove_category_icon_remove_subcategory_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('mobileno', models.CharField(default='', max_length=15)),
                ('AadharNumber', models.CharField(default='', max_length=15)),
                ('licenceNumber', models.CharField(default='', max_length=15)),
                ('appointed_to_someone', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
