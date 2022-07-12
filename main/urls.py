from django.urls import path
from .views import view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',view)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

