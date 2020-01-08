from django.urls import path
from . import views
from Truehealth import settings
from django.conf.urls.static import static

urlpatterns = [
    path('SearchDoctor', views.SearchDoctor, name='SearchDoctor'),
    path('results', views.Search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
