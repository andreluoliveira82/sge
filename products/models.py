from django.db import models
from categories.models import Category
from brands.models import Brands


class Product(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, unique=True)
    brand = models.ForeignKey(
        Brands, on_delete=models.PROTECT, verbose_name="Marca", related_name="products"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Categoría",
        related_name="products",
    )
    description = models.TextField(
        max_length=255, null=True, blank=True, verbose_name="Descrição"
    )
    serie_number = models.CharField(max_length=50, verbose_name="Número de serie")
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Custo"
    )
    salling_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço de venda"
    )
    quantity = models.IntegerField(default=0, verbose_name="Quantidade")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    is_active = models.BooleanField(default=True, verbose_name="Está ativo?")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["title"]
        indexes = [
            models.Index(fields=["title"]),
        ]

    def __str__(self):
        return self.title
