# Generated by Django 4.2.6 on 2023-10-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_katalog_bookauthor_alter_katalog_booktitle_and_more'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='buku',
            field=models.ManyToManyField(to='products.katalog'),
        ),
    ]
