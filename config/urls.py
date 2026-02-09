from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), # Inclui as URLs do aplicativo 'galeria' para lidar com rotas relacionadas à galeria de fotografias
    path('', include('usuarios.urls')), # Inclui as URLs do aplicativo 'usuarios' para lidar com rotas relacionadas a usuários
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


