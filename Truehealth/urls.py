from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Register/', include('Register.urls')),
    path('Services/', include('Services.urls')),
    path('Rules/', include('Rules.urls')),
    path('Contact/', include('Contact.urls')),
)
