# Generated by Django 4.2.4 on 2023-12-05 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patron_management',
            name='title',
        ),
        migrations.DeleteModel(
            name='book_borroewing',
        ),
        migrations.DeleteModel(
            name='book_management',
        ),
        migrations.DeleteModel(
            name='patron_management',
        ),
    ]
