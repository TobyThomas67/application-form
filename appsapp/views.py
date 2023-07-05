from django.shortcuts import render

# Create your views here.
def appli_form(request):
    return render(request,"appli_form.html")