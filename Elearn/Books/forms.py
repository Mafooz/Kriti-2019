from django import forms
from Books.models import Books

class BookuploadForm(forms.ModelForm):

	class Meta:
		model = Books
		fields = ('name','file','courses','uploaded_by')

class VerifyForm(forms.Form):
	email=forms.EmailField(max_length=200)	
	class Meta:
		fields=('email')
class OtpForm(forms.Form):
	otp=forms.IntegerField()	
	class Meta:
		fields=('otp')