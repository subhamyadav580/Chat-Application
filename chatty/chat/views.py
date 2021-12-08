from django.contrib.auth import login
from django.shortcuts import redirect, render
from chat.models import Message
# from chat.forms import RoomCreationForm

# def index(request):
#     user = request.user
#     if user.is_authenticated:
#         if request.method == 'POST':
#             form = RoomCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect(index)
#         else:
#             form = RoomCreationForm()
#     else:
#         return redirect(login)
#     return render(request, 'index.html', {'form' : form, 'username' : user.username})
def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'index.html', {'username' : user.username})
    else:
        return redirect(login)


def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25] #top 25 messages
    return render(
            request, 'chat/room.html', 
            {
                'room_name' : room_name, 
                'username' : username, 
                'messages' : messages
            }
        )
