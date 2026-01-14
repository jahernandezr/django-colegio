from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login después del registro
            return redirect('home')  # Cambia 'home' por tu página principal
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')
