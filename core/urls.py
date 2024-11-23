from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render


def home_view(request):
    return render(
        request,
        "base.html",
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("/", home_view, name="home"),
    path("", include("brands.urls")),
    path("", include("categories.urls")),
    path("", include("products.urls")),
    path("", include("inflows.urls")),
    path("", include("outflows.urls")),
]
