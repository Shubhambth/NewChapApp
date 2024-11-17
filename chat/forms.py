from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Type a message...',
                'class': 'flex-1 bg-white px-4 py-2 rounded-full shadow focus:outline-none focus:ring-2 focus:ring-purple-500',
                'autofocus': True,
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding a custom label or attributes if needed
        self.fields['body'].label = False  # Hides the label