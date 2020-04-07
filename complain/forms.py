from django import forms

from .models import storecomplain

class OurInformer(forms.ModelForm):

    email = forms.EmailField(widget=forms.EmailInput(),required=True,max_length=100)
    address =forms.CharField(widget=forms.TextInput(),required=True,max_length=120)
    description =forms.CharField(widget=forms.TextInput(),required=True,max_length=100)

    class Meta():
        model = storecomplain
        fields={
            'email',
            'address',
            'description'
        }
