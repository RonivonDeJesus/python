from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('busca', views.buscar, name='buscar'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)