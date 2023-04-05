# Generated by Django 4.1.7 on 2023-03-15 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_books_author_books_publisher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="books.author",
            ),
        ),
        migrations.AlterField(
            model_name="books",
            name="publisher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="books.publisher",
            ),
        ),
    ]
