from core.models import Cup
from django.views.generic import DetailView


class CupDetailView(DetailView):
    model = Cup
    template_name = "cup/cup_detail.html"
