# Generated by Django 5.0.6 on 2024-05-20 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_publication_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='date_added',
        ),
    ]