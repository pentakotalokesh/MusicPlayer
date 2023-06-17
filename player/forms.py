
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from player.models import Song



class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class Addsong(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'