from django import forms

class ContactForm(forms.Form):
	textWidget = forms.TextInput(attrs={'class': 'form-control'})
	messageWidget = forms.Textarea(attrs={'class': 'form-control', 'rows': '6'})
	name = forms.CharField(required=True, widget=textWidget)
	email = forms.EmailField(required=True, widget=textWidget)
	phone_number = forms.CharField(required=False, widget=textWidget, label = 'Phone Number (Optional):')
	message = forms.CharField(required=True, widget=messageWidget)