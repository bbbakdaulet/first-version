from django import forms  
from .models import Startups  
class StartupsForm(forms.ModelForm):  
    class Meta:  
        model = Startups  
        fields = ("name","about","user_id","links")
