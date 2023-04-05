# Generated by Django 4.1.7 on 2023-03-04 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_books_photo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="books",
            old_name="time_create",
            new_name="publication_date",
        ),
        migrations.RemoveField(
            model_name="books",
            name="is_published",
        ),
        migrations.RemoveField(
            model_name="books",
            name="time_updated",
        ),
    ]