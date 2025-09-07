from django import forms
from.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','category','message','attachment']
        
        
def clean_message(self):
    message = self.cleaned_data.get('message')
    if 'fuck':
        raise forms.ValidationError("Please Avoid Offesive Words")
    return message