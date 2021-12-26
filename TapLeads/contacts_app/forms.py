from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from contacts_app.models import Field



class RegistrationForm(UserCreationForm):
	name=forms.CharField(max_length=200)
	email=forms.EmailField()
	phone_number=forms.CharField(max_length=13)
	class Meta:
		model=User
		fields=("username","password1","password2")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'placeholder' : ('Name')})
		self.fields['username'].widget.attrs.update({'placeholder' : ('Username')})
		self.fields['email'].widget.attrs.update({'placeholder' : ('Email')})
		self.fields['phone_number'].widget.attrs.update({'placeholder':('Phone Number')})
		self.fields['password1'].widget.attrs.update({'placeholder':('Password')})        
		self.fields['password2'].widget.attrs.update({'placeholder':('Repeat password')})
  