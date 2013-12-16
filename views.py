#create your views here.

from django.http import HttpResponse
from django.template import loader,RequestContext

from django import forms

from django.shortcuts import redirect

class LoginForm(forms.Form):
    username=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

def dashboard(request):
    template=loader.get_template("dashboard.html")
    rc=RequestContext(request,{})
    return HttpResponse(template.render(rc))

def index(request):
    #return HttpResponse("Hello, Notes")
    if request.method=="POST":
        print "Received POST"
        form=LoginForm(request.POST)
        if form.is_valid():
            print "FORM is Valid"
            # user registration or login code
            return redirect(dashboard)
        else:
            print "FORM is NOT VALID"
            template=loader.get_template("index.html")
            rc=RequestContext(request,{'username':'Kat', 'form':form})
            return HttpResponse(template.render(rc))
    else:
        template=loader.get_template("index.html")
        rc=RequestContext(request,{'username':'Kat', 'form':LoginForm()})
        return HttpResponse(template.render(rc))

def example(request):
    template=loader.get_template("example.html")
    temp=72
    rc=RequestContext(request,{
    'fruits':['bananas','berries','kiwis'],
    'username':'Kat',
    'temp':temp})
    return HttpResponse(template.render(rc))


