# Generated by Django 3.2.6 on 2022-06-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20220614_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='locality',
            field=models.CharField(default=False, max_length=300),
            preserve_default=False,
        ),
    ]