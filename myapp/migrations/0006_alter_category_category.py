# Generated by Django 3.2.6 on 2022-05-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_product_pieces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('DealOfTheDay', 'DealOfTheDay'), ('Country chicken', 'Country Chicken'), ('Poultry chicken', 'Poultry chicken'), ('Mutton', 'Mutton'), ('Fish seafood ', 'Fish seafood'), ('Prawns', 'Prawns'), ('Cold cuts', 'Cold cuts'), ('Ready to cook', 'Ready to cook')], max_length=100),
        ),
    ]