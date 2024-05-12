from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/',include('loja.urls')),
    path('home/',include('loja.urls'))
]
