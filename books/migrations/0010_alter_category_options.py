# Generated by Django 4.1.7 on 2023-03-03 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_author_slug_field'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
