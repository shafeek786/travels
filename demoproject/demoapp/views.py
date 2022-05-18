from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="Shafy"
    return render(request,"index.html",{"ss":name})

def forms(request):
    return render(request,"forms.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("Contact Us")
def thanks(request):
    return HttpResponse("Thank You")
def results(request):
    a = int(request.GET['number1'])
    b = int(request.GET['number2'])
    res=a+b
    res1=a*b
    res2=a/b
    return render(request,"results.html",{"result":res,"results1":res1,"results2":res2})
