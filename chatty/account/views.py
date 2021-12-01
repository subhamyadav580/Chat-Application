from django.shortcuts import render
from account.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})
