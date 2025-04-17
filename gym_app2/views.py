from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Agrega aquí tu lógica de autenticación
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
