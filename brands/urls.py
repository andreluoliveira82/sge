from django.urls import path
from . import views

urlpatterns = [
    path("brands/list/", views.BrandListView.as_view(), name="brand_list"),
    path("brands/create/", views.BrandCreateView.as_view(), name="brand_create"),
    path(
        "brands/<int:pk>/details/",
        views.BrandDetailsView.as_view(),
        name="brand_details",
    ),
    path(
        "brands/<int:pk>/update/",
        views.BrandUpdateView.as_view(),
        name="brand_update",
    ),
    path(
        "brands/<int:pk>/delete/",
        views.BrandDeleteView.as_view(),
        name="brand_delete",
    ),
]
