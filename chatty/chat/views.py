from django.shortcuts import render
from chat.models import Message
from chatty.chat.forms import RoomCreationForm

def index(request):
    form = RoomCreationForm()
    return render(request, 'index.html', {'form' : form})

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25] #top 25 messages

    return render(request, 'chat/room.html', {'room_name' : room_name, 'username' : username, 'messages' : messages})
