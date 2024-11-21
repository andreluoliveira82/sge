from django.db import models


class Brands(models.Model):
    name = models.CharField(verbose_name="Marca", max_length=50)
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)
    is_active = models.BooleanField(verbose_name="Está ativo?", default=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["name"]

    def __str__(self):
        return self.name
