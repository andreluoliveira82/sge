from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import Brands
from .forms import BrandForm


class BrandListView(ListView):
    model = Brands
    template_name = "brand_list.html"
    context_object_name = "brands"
    paginate_by = 10

    def get_queryset(self):
        """
        Filtra o queryset com base no parâmetro 'name' na query string.
        """
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(CreateView):
    model = Brands
    template_name = "brand_create.html"
    context_object_name = "brands"
    form_class = BrandForm
    success_url = reverse_lazy("brand_list")
    extra_context = {"title": "Criar Marca"}
    success_message = "Marca criada com sucesso!"
    error_message = "Erro ao criar marca!"
    success_status = 201
    error_status = 400
    success_template = "brand_create_success.html"
    error_template = "brand_create_error.html"
    success_context = {"message": "Marca criada com sucesso!"}
    error_context = {"message": "Erro ao criar marca!"}
    success_redirect = reverse_lazy("brand_list")
    error_redirect = reverse_lazy("brand_list")
    success_message_code = 201
    error_message_code = 400
    success_message_code_name = "Created"
    error_message_code_name = "Bad Request"
    success_message_code_description = "Created"


class BrandDetailsView(DetailView):
    model = Brands
    template_name = "brand_details.html"
    context_object_name = "brand"
    extra_context = {"title": "Detalhes da Marca"}
    success_message = "Marca detalhada com sucesso!"
    error_message = "Erro ao detalhar marca!"
    success_status = 200
    error_status = 404
    success_template = "brand_details_success.html"
    error_template = "brand_details_error.html"
    success_context = {"message": "Marca detalhada com sucesso!"}
    error_context = {"message": "Erro ao detalhar marca!"}
    success_redirect = reverse_lazy("brand_list")
    error_redirect = reverse_lazy("brand_list")
    success_message_code = 200
    error_message_code = 404
    success_message_code_name = "OK"
    error_message_code_name = "Not Found"
    success_message_code_description = "OK"


class BrandUpdateView(UpdateView):
    model = Brands
    template_name = "brand_update.html"
    context_object_name = "brand"
    form_class = BrandForm
    success_url = reverse_lazy("brand_list")
    extra_context = {"title": "Atualizar Marca"}
    success_message = "Marca atualizada com sucesso!"
    error_message = "Erro ao atualizar marca!"
    success_status = 200
    error_status = 400
    success_template = "brand_update_success.html"
    error_template = "brand_update_error.html"
    success_context = {"message": "Marca atualizada com sucesso!"}
    error_context = {"message": "Erro ao atualizar marca!"}
    success_redirect = reverse_lazy("brand_list")
    error_redirect = reverse_lazy("brand_list")
    success_message_code = 200
    error_message_code = 400
    success_message_code_name = "OK"


class BrandDeleteView(DeleteView):
    model = Brands
    template_name = "brand_delete.html"
    context_object_name = "brand"
    success_url = reverse_lazy("brand_list")
    extra_context = {"title": "Excluir Marca"}
    success_message = "Marca excluida com sucesso!"
    error_message = "Erro ao excluir marca!"
    success_status = 200
    error_status = 400
    success_template = "brand_delete_success.html"
    error_template = "brand_delete_error.html"
    success_context = {"message": "Marca excluida com sucesso!"}
    error_context = {"message": "Erro ao excluir marca!"}
    success_redirect = reverse_lazy("brand_list")
    error_redirect = reverse_lazy("brand_list")
    success_message_code = 200
    error_message_code = 400
    success_message_code_name = "OK"
