"""shelter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from shelter_app.views import PetView, PetViewDetail, AboutView
from django.views.generic import RedirectView
from django_filters.views import FilterView
from shelter_app.filters import PetFilter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AboutView.as_view()),
    path('filter/<str:pk>/', PetViewDetail.as_view()),
    path('about/', AboutView.as_view()),
    path(
        "favicon.ico",
        RedirectView.as_view(url=static("favicon.ico"))
    ),
    path('filter/', FilteredView.as_view()),
]
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
