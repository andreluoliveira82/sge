from django.db import models
from products.models import Product


class Inflow(models.Model):
    """Gerencia saidas de produtos."""

    product = (
        models.ForeignKey(
            Product,
            on_delete=models.PROTECT,
            verbose_name="Produto",
            related_name="inflows",
        ),
    )
    quantity = (models.IntegerField(verbose_name="Quantidade"),)
    descripition = models.TextField(verbose_name="Descrição", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)
