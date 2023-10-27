# Generated by Django 4.2.6 on 2023-10-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_katalog_bookauthor_alter_katalog_booktitle_and_more'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='owned_books',
            field=models.ManyToManyField(related_name='owned_books', to='products.katalog'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cart',
            field=models.ManyToManyField(related_name='cart', to='products.katalog'),
        ),
    ]