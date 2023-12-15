from core.models import Cup
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class CupCreateView(CreateView):
    model = Cup
    fields = "__all__"
    template_name = "cup/cup_create.html"
    success_url = reverse_lazy("cup_list")
