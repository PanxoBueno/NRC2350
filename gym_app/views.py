from django.shortcuts import render, redirect, get_object_or_404
from .forms import AtletaForm, EntrenadorForm, BibliotecaForm, ClaseForm, ReservaForm
from .models import Atleta, Entrenador, Biblioteca, Clase, Reserva

def home(request):
    biblioteca = Biblioteca.objects.all()
    data={
        'ejercicios': biblioteca
    }
    return render(request, 'home.html', data)

def menu(request):
    atletas = Atleta.objects.all()
    entrenadores = Entrenador.objects.all()
    context = {'atletas': atletas, 'entrenadores': entrenadores}
    return render(request, 'menu.html', context)

def crear_atleta(request):
    if request.method == 'POST':
        form = AtletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = AtletaForm()
    return render(request, 'create_atleta.html', {'form': form})

def modificar_atleta(request, pk):
    atleta = get_object_or_404(Atleta, pk=pk)
    if request.method == 'POST':
        form = AtletaForm(request.POST, instance=atleta)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = AtletaForm(instance=atleta)
    return render(request, 'update_atleta.html', {'form': form, 'atleta': atleta})

def borrar_atleta(request, pk):
    atleta = get_object_or_404(Atleta, pk=pk)
    if request.method == 'POST':
        atleta.delete()
        return redirect('menu')
    return render(request, 'delete_atleta.html', {'atleta': atleta})

def crear_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = EntrenadorForm()
    return render(request, 'create_entrenador.html', {'form': form})

def modificar_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = EntrenadorForm(instance=entrenador)
    return render(request, 'update_entrenador.html', {'form': form, 'entrenador': entrenador})

def borrar_entrenador(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    if request.method == 'POST':
        entrenador.delete()
        return redirect('menu')
    return render(request, 'delete_entrenador.html', {'entrenador': entrenador})

def crear_biblioteca(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, request.FILES)  # Importante incluir request.FILES
        if form.is_valid():
            form.save()
            return redirect('menu')  # Redirige a donde necesites
    else:
        form = BibliotecaForm()
    
    return render(request, 'create_biblioteca.html', {'form': form})

#aca reservas
def crear_clase(request):
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = ClaseForm()
    return render(request, 'create_clase.html', {'form': form})

def listar_clases(request):
    clases = Clase.objects.all().order_by('fecha', 'horario')
    return render(request, 'list_clases.html', {'clases': clases})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Verificar capacidad de la clase
            clase = form.cleaned_data['clase']
            reservas_count = Reserva.objects.filter(clase=clase).count()
            if reservas_count >= clase.capacidad_maxima:
                form.add_error('clase', 'Esta clase ha alcanzado su capacidad máxima')
            else:
                form.save()
                return redirect('ver_reservas')
    else:
        form = ReservaForm()
    return render(request, 'create_reserva.html', {'form': form})

def ver_reservas(request):
    # Reservas agrupadas por atleta
    reservas_por_atleta = {}
    for atleta in Atleta.objects.all():
        reservas = Reserva.objects.filter(atleta=atleta)
        if reservas.exists():
            reservas_por_atleta[atleta] = reservas
    
    # Total de atletas por clase
    clases_con_atletas = []
    for clase in Clase.objects.all():
        count = Reserva.objects.filter(clase=clase).count()
        clases_con_atletas.append({
            'clase': clase,
            'count': count,
            'porcentaje': (count / clase.capacidad_maxima) * 100 if clase.capacidad_maxima > 0 else 0
        })
    
    context = {
        'reservas_por_atleta': reservas_por_atleta,
        'clases_con_atletas': clases_con_atletas,
    }
    return render(request, 'view_reservas.html', context)