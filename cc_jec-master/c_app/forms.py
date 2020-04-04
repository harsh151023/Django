from django import forms
from c_app.models import User

class NewUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    semester = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Semester'}))
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Branch'}))
    town = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Town/City'}))
    contact = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact'}))    
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail'}))




    class Meta():
        model = User
        fields = '__all__'
