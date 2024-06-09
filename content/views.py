from django.shortcuts import render

# Create your views here.

def home(request):
    context = {"title": "home"}
    return render(request, 'content/home.html', context)

def about(request):
    context = {"title": "about"}
    return render(request, 'content/about.html', context)

def services(request):
    context = {"title": "services"}
    return render(request, 'content/services.html', context)

def contact(request):
    context = {"title": "contact"}
    return render(request, 'content/contact.html', context)
