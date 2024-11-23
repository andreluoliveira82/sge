from django.urls import path
from . import views

urlpatterns = [
    path("suppliers/list/", views.SupplierListView.as_view(), name="supplier_list"),
    path(
        "suppliers/create/", views.SupplierCreateView.as_view(), name="supplier_create"
    ),
    path(
        "suppliers/<int:pk>/details/",
        views.SupplierDetailsView.as_view(),
        name="supplier_details",
    ),
    path(
        "suppliers/<int:pk>/update/",
        views.SupplierUpdateView.as_view(),
        name="supplier_update",
    ),
    path(
        "suppliers/<int:pk>/delete/",
        views.SupplierDeleteView.as_view(),
        name="supplier_delete",
    ),
]
