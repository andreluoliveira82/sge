from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"
    paginate_by = 10

    def get_queryset(self):
        """
        Filtra o queryset com base no parâmetro 'name' na query string.
        """
        queryset = super().get_queryset().order_by("id")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "supplier_create.html"
    context_object_name = "suppliers"
    form_class = SupplierForm
    success_url = reverse_lazy("supplier_list")
    extra_context = {"title": "Criar Fornecedor"}
    success_message = "Fornecedor criado com sucesso!"
    error_message = "Erro ao criar fornecedor!"
    success_status = 201
    error_status = 400
    success_template = "supplier_create_success.html"
    error_template = "supplier_create_error.html"
    success_context = {"message": "Fornecedor criado com sucesso!"}
    error_context = {"message": "Erro ao criar fornecedor!"}
    success_redirect = reverse_lazy("supplier_list")
    error_redirect = reverse_lazy("supplier_list")
    success_message_code = 201
    error_message_code = 400
    success_message_code_name = "Created"
    error_message_code_name = "Bad Request"
    success_message_code_description = "Created"


class SupplierDetailsView(DetailView):
    model = Supplier
    template_name = "supplier_details.html"
    context_object_name = "supplier"
    extra_context = {"title": "Detalhes da Fornecedor"}
    success_message = "Fornecedor detalhada com sucesso!"
    error_message = "Erro ao detalhar fornecedor!"
    success_status = 200
    error_status = 404
    success_template = "supplier_details_success.html"
    error_template = "supplier_details_error.html"
    success_context = {"message": "Fornecedor detalhada com sucesso!"}
    error_context = {"message": "Erro ao detalhar fornecedor!"}
    success_redirect = reverse_lazy("supplier_list")
    error_redirect = reverse_lazy("supplier_list")
    success_message_code = 200
    error_message_code = 404
    success_message_code_name = "OK"
    error_message_code_name = "Not Found"
    success_message_code_description = "OK"


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "supplier_update.html"
    context_object_name = "supplier"
    form_class = SupplierForm
    success_url = reverse_lazy("supplier_list")
    extra_context = {"title": "Atualizar Fornecedor"}
    success_message = "Fornecedor atualizado  com sucesso!"
    error_message = "Erro ao atualizar fornecedor!"
    success_status = 200
    error_status = 400
    success_template = "supplier_update_success.html"
    error_template = "supplier_update_error.html"
    success_context = {"message": "Fornecedor atualizadao com sucesso!"}
    error_context = {"message": "Erro ao atualizar fornecedor!"}
    success_redirect = reverse_lazy("supplier_list")
    error_redirect = reverse_lazy("supplier_list")
    success_message_code = 200
    error_message_code = 400
    success_message_code_name = "OK"


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplier_delete.html"
    context_object_name = "supplier"
    success_url = reverse_lazy("supplier_list")
    extra_context = {"title": "Excluir Fornecedor"}
    success_message = "Fornecedor excluida com sucesso!"
    error_message = "Erro ao excluir fornecedor!"
    success_status = 200
    error_status = 400
    success_template = "supplier_delete_success.html"
    error_template = "supplier_delete_error.html"
    success_context = {"message": "Fornecedor excluida com sucesso!"}
    error_context = {"message": "Erro ao excluir fornecedor!"}
    success_redirect = reverse_lazy("supplier_list")
    error_redirect = reverse_lazy("supplier_list")
    success_message_code = 200
    error_message_code = 400
    success_message_code_name = "OK"
