from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50)
    #phone = forms.IntegerField()
    form_email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
