from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('juegos', juegos, name='juegos'),
    path('noticias', noticias, name='noticias'),
    path('deportes', deportes, name='deportes'),
    path('contacto', contact, name='contacto'),
    path('contacto/exito/', contact_success, name='contact_success'),
    path('politicas', terminos, name='terminos'),
    path('uso-contenido', uso_content, name='uso_content'),
    path('nosotros', nosotros, name='nosotros'),
]
