from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/home.html')



def about(request):
    return render(request, 'core/about.html')


def resume(request):
    return render(request, 'core/resume.html')


def services(request):
    return render(request, 'core/services.html')


def contact(request):
    return render(request, 'core/contact.html')