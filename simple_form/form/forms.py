from django import forms
from .models import Message



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender_email', 'message']

        widgets = {
            'sender_email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'type': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message'}),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError('This field is required')
        return message
