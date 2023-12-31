from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from confid import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('categoria/', include('categoria.urls')),
    path('magazin/', include('magazin.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)