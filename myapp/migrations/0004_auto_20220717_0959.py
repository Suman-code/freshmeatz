# Generated by Django 3.2.6 on 2022-07-17 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_ordeitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrdeItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
