from core.models import Cup
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class CupUpdateView(UpdateView):
    model = Cup
    fields = "__all__"
    template_name = "cup/cup_update.html"
    success_url = reverse_lazy("cup_list")
