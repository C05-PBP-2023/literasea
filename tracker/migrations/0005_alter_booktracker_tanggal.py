# Generated by Django 4.2.6 on 2023-10-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_rename_nama_buku_booktracker_judul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktracker',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]