from core.models import Cup
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class CupDeleteView(DeleteView):
    model = Cup
    template_name = "cup/cup_delete.html"
    success_url = reverse_lazy("cup_list")
