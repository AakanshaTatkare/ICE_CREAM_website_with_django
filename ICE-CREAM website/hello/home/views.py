from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    contex ={
        'variable':"this is sent"   #sending variable to the template#context is set of variables you sent on templates
    }
    return render(request,'index.html',contex) #we renderd the template here
    # return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')
        contact = Contact(name=name,email=email,phone=phone,reason=reason,date=datetime.today())#made an object
        contact.save()
        messages.success(request, "your message has been sent.")
    
    return render(request,'contact.html')
