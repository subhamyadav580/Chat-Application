from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Username'
            }
        ))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
            attrs={
                'style': 'height:40px;',
                'placeholder' : 'Email'
            }
        ))
    password = forms.PasswordInput()

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if not username and not email:
            raise forms.ValidationError('You have to write something!')