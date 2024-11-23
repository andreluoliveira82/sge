from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "brand",
        "category",
        "cost_price",
        "salling_price",
        "quantity",
        "is_active",
    )
    list_filter = (
        "is_active",
        "category",
        "brand",
    )
    search_fields = (
        "name",
        "serie_number",
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["title"]

    def __str__(self):
        return self.title
