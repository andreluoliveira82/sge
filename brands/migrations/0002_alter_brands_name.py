# Generated by Django 5.1.3 on 2024-11-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Marca'),
        ),
    ]
