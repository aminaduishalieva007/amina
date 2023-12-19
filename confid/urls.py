from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('categoria/', include('categoria.urls')),
    path('magazin/', include('magazin.urls'))
    
]

