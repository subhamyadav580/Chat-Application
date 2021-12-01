from django import forms
from django.db.models import fields

from chat.models import Room

class RoomCreationForm(forms.Form):
    room_name = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Room Name'
            }
    ))
    room_password = forms.CharField(max_length=254, widget=forms.PasswordInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Room Password'
            }
    ))

    class Meta:
        model = Room
        fields = ['room_name', 'room_password']

    def save(self, commit=True):
        room_instance = self.instance
        room_instance.room_name = self.cleaned_data['room_name']
        room_instance.room_password = self.cleaned_data['room_password']

        if commit:
            room_instance.save()
            
        return room_instance