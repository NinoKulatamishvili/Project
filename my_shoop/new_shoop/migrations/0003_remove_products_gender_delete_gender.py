# Generated by Django 5.0.6 on 2024-07-04 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_shoop', '0002_gender_products_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='gender',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]