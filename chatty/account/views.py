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

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect(index)
        else:
            return render(request, 'auth/login.html')
    else:
        return render(request, 'auth/login.html')