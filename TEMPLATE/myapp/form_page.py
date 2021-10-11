from django import forms
class College(forms.Form):

	Name=forms.CharField()
	FatherName=forms.CharField()
	MotherName=forms.CharField()
	Phone = forms.IntegerField()
	Email=forms.EmailField()
	Address=forms.CharField()
	