from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Truehealth import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Services/', include('Services.urls')),
    path('Rules/', include('Rules.urls')),
    path('Contact/', include('Contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
