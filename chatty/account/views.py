from django.shortcuts import redirect, render
from account.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(email, username, password)
        return render(request, 'chat/room.html')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})
