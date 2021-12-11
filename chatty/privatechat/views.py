from django.shortcuts import render

def privatechat(request):
    return render(request, 'private/privatechat.html')