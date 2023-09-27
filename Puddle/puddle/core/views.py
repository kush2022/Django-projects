from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from item.models import Category, Item
from . forms import SignUpForm, LoginForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html',  context=context)


def contact(request):
    return render(request, 'core/contact.html')



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    
    form = SignUpForm()
    context = {
        'form': form 
    }

    return render(request, 'core/signup.html', context=context)


def login_request(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            return redirect('core:index')
    form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'core/login.html', context=context)