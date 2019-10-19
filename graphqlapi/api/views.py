from django.shortcuts import render

# Create your views here.

def index(request):
    data={}
    
    
    return render(request,'pages/categorie.html',data)

def detail(request):
    data={}
    
    
    return render(request,'pages/detail.html',data)




def ingredient(request):
    data={}
    
    
    return render(request,'pages/ingredient.html',data)