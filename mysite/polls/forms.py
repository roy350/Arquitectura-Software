from django import forms
from .models import Message
from datetime import datetime

class Form(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
            'text',
            'ip',
        ]
        labels = {
            'text' : 'Mensaje',
            'ip': 'Ip',
        }
