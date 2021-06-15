import django_filters
from shelter_app.models import Pet
from django import forms

class PetFilter(django_filters.FilterSet):
    # pet_name = django_filters.CharFilter(lookup_expr='icontains')
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Pet.objects.all())
    # widget = forms.CheckboxSelectMultiple()

    class Meta:
        model = Pet
        fields = ['name', 'kind', 'age']
