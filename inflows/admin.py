from django.contrib import admin
from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "supplier",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "product",
        "supplier",
    )
    search_fields = ("product",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created_at"]

    def __str__(self):
        return self.product
