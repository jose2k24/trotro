from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'admin/base_site.html')


def home(request):
    return render(request,'admin/home.html')
    
def about(request):
    return render(request,'admin/about.html') 
       
def contact(request):
    return render(request,'admin/contact.html') 

def geocode(request):
    return render(request,'admin/geocode.html')

def service(request):
    return render(request,'admin/service.html') 

def faq(request):
    return render(request,'admin/faq.html')   

