from django.contrib import admin
from .models import Brands


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    list_filter = ("name", "description",)
    search_fields = (
        "name",
        "description",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ("name",)
        list_per_page = 10
        list_max_show_all = 100
        date_hierarchy = "created_at"
        