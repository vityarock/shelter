from django.contrib import admin
from shelter_app.models import Pet
# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    
    @staticmethod
    def pet_name(obj):
        return obj.pet.name