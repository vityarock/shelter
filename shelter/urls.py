from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from shelter_app.views import PetView, PetViewDetail, AboutView, FilteredView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index),
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
