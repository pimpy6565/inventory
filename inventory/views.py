from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):

    post = flavor.objects.all()
    form = ReceiveStockForm()
    return render(request,'inventory/index.html',{
        "post":post,
       "form":form
    })

def LoginV(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return HttpResponseRedirect(reverse('index'))
    else: 
        form = AuthenticationForm()      
        return render(request,'inventory/login.html',{
            "form":form
        })

def create(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render(request,'inventory/newuser.html',{
        "form":form
    })

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def newf(request):
    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        cost = request.POST['cost']
        units = request.POST['units']
        new_flavor = flavor(name = name.upper(),category = category.upper(),cost = cost,units = units)
        new_flavor.save()
        return HttpResponseRedirect(reverse('newf'))
    else:
        form = ReceiveStockForm()
        return render(request,'inventory/newf.html',{
            "form":form
        })

def addunits(request):
    if request.method == "POST":
        form = ReceiveStockForm(request.POST)
        if form.is_valid():
            flavor = form.cleaned_data['flavor']
            amount = form.cleaned_data['quantity']
            flavor.receive(amount)
            messages.success(request, f"{amount} units added to {flavor}.")
            return HttpResponseRedirect(reverse('index'))
    else:
        return messages.ERROR

def edit(request):
    post = flavor.objects.all
    form = ReceiveStockForm()
    return render(request,'inventory/edit.html',{
        "post":post,
        "form":form
    })

def editb(request,id):
    myflav = flavor.objects.get(pk=id)
    if len(request.POST['name']) > 0:
        myflav.name = request.POST['name'].upper()
        myflav.save()
    if len(request.POST['category']) > 0:
        myflav.category = request.POST['category'].upper()
        myflav.save()
    if len(request.POST['units']) > 0:   
        myflav.units = request.POST['units']
        myflav.save()
    if len(request.POST['cost']) > 0:
        myflav.cost = request.POST['cost']
        myflav.save()
    else:
       return HttpResponseRedirect(reverse('edit')) 
    
    return HttpResponseRedirect(reverse('edit'))

def delp(request,id):
    if request.method == "DELETE":
        item = flavor.objects.get(pk=id)
        item.delete()
        return JsonResponse({'Flavor Deleted!'})
    else:
        return JsonResponse({'Error'})

    
def cat(request):
    post = flavor.objects.all()
    form = ReceiveStockForm()
    catlist = []
    for i in post:
        if i.category.upper() not in catlist:
            catlist.append(i.category)
        else:
            pass
    return render(request,'inventory/category.html',{
        "post":catlist,
        "form":form
    })

def select(request,cat):
    form =ReceiveStockForm()
    if request.method == "GET":
        post = flavor.objects.filter(category=cat.upper())
        
        return render(request,"inventory/select.html",{
            "post":post,
            "form":form
        })
    

def search(request):
    if request.method == "GET":
        post = flavor.objects.filter(name=request.GET.get('q').upper())
        print(post)
        return render(request,"inventory/search.html",{
            "post":post
        })