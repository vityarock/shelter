from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from shelter_app.models import Pet
from .filters import PetFilter
# Create your views here.


class PetView(ListView):
    model = Pet
    template_name = "pet_list.html"

    def get_queryset(self):
        qs = self.model.objects.all()
        pet_filtered_list = PetFilter(self.request.GET, queryset=qs)
        return pet_filtered_list.qs


class PetViewDetail(DetailView):
    model = Pet
    template_name = "pet_detail.html"