# Generated by Django 4.2.5 on 2023-10-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_book_reviewed_question_book_asked'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
