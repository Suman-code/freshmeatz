# Generated by Django 3.2.6 on 2022-05-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Deal_of_The_Day', 'Deal_Of_The_Day'), ('Country_chicken', 'Country_Chicken'), ('Poultry_chicken', 'Poultry_chicken'), ('Mutton', 'Mutton'), ('Fish_seafood ', 'Fish_seafood'), ('Prawns', 'Prawns'), ('Cold_cuts', 'Cold_cuts'), ('Ready_to_cook', 'Ready_to_cook')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Deal_of_The_Day', 'Deal_Of_The_Day'), ('Country_chicken', 'Country_Chicken'), ('Poultry_chicken', 'Poultry_chicken'), ('Mutton', 'Mutton'), ('Fish_seafood ', 'Fish_seafood'), ('Prawns', 'Prawns'), ('Cold_cuts', 'Cold_cuts'), ('Ready_to_cook', 'Ready_to_cook')], max_length=100),
        ),
    ]
