from django.shortcuts import redirect, render
from chat.models import Message
from chat.forms import RoomCreationForm

def index(request):
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = RoomCreationForm()
    return render(request, 'index.html', {'form' : form})

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25] #top 25 messages

    return render(request, 'chat/room.html', {'room_name' : room_name, 'username' : username, 'messages' : messages})
