# Generated by Django 3.1.7 on 2021-03-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20210303_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='individual',
            options={'ordering': ['surname1']},
        ),
        migrations.AddField(
            model_name='entity',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
    ]