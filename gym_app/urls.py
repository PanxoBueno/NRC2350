from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('biblioteca/', views.home, name='biblioteca'),
    path('crear_biblioteca/', views.crear_biblioteca, name='crear_biblioteca'),
    path('crear_atleta/', views.crear_atleta, name='crear_atleta'),
    path('modificar_atleta/<int:pk>/', views.modificar_atleta, name='modificar_atleta'),
    path('borrar_atleta/<int:pk>/', views.borrar_atleta, name='borrar_atleta'),
    path('crear_entrenador/', views.crear_entrenador, name='crear_entrenador'),
    path('modificar_entrenador/<int:pk>/', views.modificar_entrenador, name='modificar_entrenador'),
    path('borrar_entrenador/<int:pk>/', views.borrar_entrenador, name='borrar_entrenador'),

#REservar
    path('crear_clase/', views.crear_clase, name='crear_clase'),
    path('listar_clases/', views.listar_clases, name='listar_clases'),
    path('crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('ver_reservas/', views.ver_reservas, name='ver_reservas'),
]
    