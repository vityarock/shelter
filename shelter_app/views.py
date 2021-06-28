from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.base import TemplateView
from shelter_app.models import Pet
from .filters import PetFilter
# Create your views here.


class PetView(ListView):
    model = Pet
    template_name = "pet_list.html"

class FilteredView(ListView):
    model = Pet
    template_name = "pet_filter.html"
    context_object_name = "pets"
    paginate_by = 3

    def get_filter(self):
        return PetFilter(self.request.GET, queryset=super().get_queryset())
        
    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter(),
        }


class PetViewDetail(DetailView):
    model = Pet
    template_name = "pet_detail.html"


class AboutView(TemplateView):
    template_name = "about.html"
