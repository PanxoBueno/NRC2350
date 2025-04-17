from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Entrenador, Atleta, Clase, Reserva
from .forms import EntrenadorForm, AtletaForm, ClaseForm, ReservaForm

# Vistas para Entrenadores
class EntrenadorListView(ListView): 
    model = Entrenador
    template_name = 'gestion/entrenadores/list.html'

class EntrenadorCreateView(CreateView):
    model = Entrenador
    form_class = EntrenadorForm
    success_url = reverse_lazy('entrenadores_list')
    template_name = 'gestion/entrenadores/form.html'

# (Repetir para UpdateView y DeleteView)
class EntrenadorUpdateView(UpdateView):
    model = Entrenador
    form_class = EntrenadorForm
    template_name = 'gestion/entrenadores/form.html'
    success_url = reverse_lazy('entrenadores_list')

class EntrenadorDeleteView(DeleteView):
    model = Entrenador
    template_name = 'gestion/entrenadores/confirm_delete.html'
    success_url = reverse_lazy('entrenadores_list')

# Vistas COMPLETAS para Atleta
class AtletaListView(ListView):
    model = Atleta
    template_name = 'gestion/atletas/list.html'

class AtletaCreateView(CreateView):
    model = Atleta
    form_class = AtletaForm
    template_name = 'gestion/atletas/form.html'
    success_url = reverse_lazy('atletas_list')

class AtletaUpdateView(UpdateView):
    model = Atleta
    form_class = AtletaForm
    template_name = 'gestion/atletas/form.html'
    success_url = reverse_lazy('atletas_list')

class AtletaDeleteView(DeleteView):
    model = Atleta
    template_name = 'gestion/atletas/confirm_delete.html'
    success_url = reverse_lazy('atletas_list')
# Vistas similares para Atleta y Clase

# Vista para reservas
def reservar_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.atleta = request.user.atleta
            reserva.save()
            return redirect('horarios')
    else:
        form = ReservaForm(initial={'clase': clase})
    return render(request, 'gestion/reservas/form.html', {'form': form})