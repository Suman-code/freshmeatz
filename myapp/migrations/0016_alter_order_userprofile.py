# Generated by Django 3.2.6 on 2022-07-21 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_order_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='userprofile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.userprofile'),
        ),
    ]
