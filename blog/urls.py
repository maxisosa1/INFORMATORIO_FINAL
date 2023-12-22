
from django.contrib import admin
from django.urls import path, include
from . import views
#URL LOGIN
from django.contrib.auth import views as auth

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    # 1 PARAMETROS ES EL TEXTO DE LA URL
    # 2 LA VISTA QUE VA EJECUTAR
    # 3 ES EL NOMBRE LA URL (aun no lo usamos)
    path('', views.Home, name = 'home'),
    #No necesariamente estos 3 valores (parametors) se deben llamar igual
    path('Nosotros/', views.Nosotros, name = 'nosotros'),

    #LOGIN
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),

    # URL DE APLICACION
    path('Noticias/', include('apps.noticias.urls')),
    path('Usuario/',include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

