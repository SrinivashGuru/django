from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
def homepage(request):
    form = my_class_form()
    # srini = [1,2,3,4]
    context={
        "dev_name": " Username : Srini",
        "address": "Adress : Phily",
        "display_form": form
    }
    if request.method=='POST':
        form=my_class_form(request.POST)
        if form.is_valid():
            form.save()
            global name
            name= form.cleaned_data.get('name')
        return redirect('hey')

    return render(request, 'home.html',context)

def name(request):
    if name=="thiru":
        context = {"myname": "Mamiyar"}
    elif name=="THIRU":
        context = {"myname": "Mamiyar"}
    elif name == "Thiru":
        context = {"myname": "Mamiyar"}
    else:
        context={"myname":name}
    return render(request, 'home1.html', context)