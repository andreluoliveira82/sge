from django.db import models
from suppliers.models import Supplier
from products.models import Product


class Outflow(models.Model):
    """Gerencia saidas de produtos."""

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        verbose_name="Fornecedor",
        related_name="outflows",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Produto",
        related_name="outflows",
    )
    quantity = models.IntegerField(verbose_name="Quantidade")
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Saida"
        verbose_name_plural = "Saidas"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)
