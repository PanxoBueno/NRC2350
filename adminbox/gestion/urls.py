from django.urls import path
from gestion.views import EntrenadorListView, EntrenadorCreateView, EntrenadorUpdateView,EntrenadorDeleteView, AtletaUpdateView, AtletaListView, AtletaCreateView, AtletaDeleteView 

urlpatterns = [
    path('entrenadores/', EntrenadorListView.as_view(), name='entrenadores_list'),
    path('entrenadores/nuevo/', EntrenadorCreateView.as_view(), name='entrenador_create'),
    # Agregar más URLs para Atletas, Clases, etc.
     # Entrenadores
    path('entrenadores/', EntrenadorListView.as_view(), name='entrenadores_list'),
    path('entrenadores/nuevo/', EntrenadorCreateView.as_view(), name='entrenador_create'),
    path('entrenadores/editar/<int:pk>/', EntrenadorUpdateView.as_view(), name='entrenador_update'),
    path('entrenadores/eliminar/<int:pk>/', EntrenadorDeleteView.as_view(), name='entrenador_delete'),
    
    # Atletas
    path('atletas/', AtletaListView.as_view(), name='atletas_list'),
    path('atletas/nuevo/', AtletaCreateView.as_view(), name='atleta_create'),
    path('atletas/editar/<int:pk>/', AtletaUpdateView.as_view(), name='atleta_update'),
    path('atletas/eliminar/<int:pk>/', AtletaDeleteView.as_view(), name='atleta_delete'),
]