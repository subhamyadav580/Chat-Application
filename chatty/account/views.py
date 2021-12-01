from django.shortcuts import redirect, render
from account.forms import RegisterForm
from chat.views import index

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})
