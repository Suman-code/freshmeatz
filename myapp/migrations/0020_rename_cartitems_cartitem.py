# Generated by Django 3.2.6 on 2022-07-03 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_cart_cartitems'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItems',
            new_name='CartItem',
        ),
    ]
