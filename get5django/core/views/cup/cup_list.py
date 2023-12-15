from core.models import Cup
from django.views.generic import ListView


class CupListView(ListView):
    model = Cup
    template_name = "cup/cup_list.html"
