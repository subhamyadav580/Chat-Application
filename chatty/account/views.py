from django.shortcuts import redirect, render
from account.forms import RegisterForm
from chat.views import index
from django.contrib.auth import login, authenticate, logout

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def register(request):
    user = request.user
    if user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect(index)
        else:
            return render(request, 'auth/login.html')
    else:
        return render(request, 'auth/login.html')