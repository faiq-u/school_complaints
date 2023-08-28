from django.forms import ModelForm
from .models import complaints
from django.contrib.auth.models import User

class complaintsform(ModelForm):
    class Meta():
        model=complaints
        fields=['actual','anonyomous','about']
        
   
class passornot(ModelForm):
    class Meta():
        model = complaints
        fields = ['acceptable']

class princord(ModelForm):
    class Meta():
        model = complaints
        fields = ['rejected1','fixed']
