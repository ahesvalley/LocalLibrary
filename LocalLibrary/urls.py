from django import urls
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('catalog/admin/', admin.site.urls, name='admin'),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', include('search.urls'))
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)