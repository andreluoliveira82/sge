# Generated by Django 5.1.3 on 2024-11-21 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0002_alter_brands_name'),
        ('categories', '0002_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Título')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descrição')),
                ('serie_number', models.CharField(max_length=50, verbose_name='Número de serie')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Custo')),
                ('salling_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço de venda')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('is_active', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='brands.brands', verbose_name='Marca')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='categories.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['title'],
                'indexes': [models.Index(fields=['title'], name='products_pr_title_7d8124_idx')],
            },
        ),
    ]
