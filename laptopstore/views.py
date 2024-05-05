from django.shortcuts import render
from laptopstore.models import Contact
# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")
        myquery = Contact()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')