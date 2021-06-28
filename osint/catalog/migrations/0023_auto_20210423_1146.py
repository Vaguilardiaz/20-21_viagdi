# Generated by Django 3.1.7 on 2021-04-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20210416_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='start_date',
            field=models.DateField(blank=True, help_text='Fecha en la que empezó con el cargo', null=True, verbose_name='Desde'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='untill',
            field=models.DateField(blank=True, help_text='Fecha de cese', null=True, verbose_name='Hasta'),
        ),
    ]