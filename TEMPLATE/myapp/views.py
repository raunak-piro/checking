from django.shortcuts import render
from myapp import form_page
def index(request):
	var=form_page.College()
	dic={'key':var}
	return render(request,"silver.html",context=dic)
# Create your views here.
