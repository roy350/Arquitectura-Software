from django import forms
from .models import Message
from datetime import datetime

class Form(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
            'text',
            'ip',
            'pub_date'
        ]
        labels = {
            'text' : 'Mensaje',
            'ip': 'Ip',
            'pub_date': 'Pub_date'
        }
