# Generated by Django 3.1.7 on 2021-04-24 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20210424_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note',
            new_name='text',
        ),
    ]