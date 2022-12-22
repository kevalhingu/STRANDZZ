from pickle import TRUE
import re
from symbol import return_stmt
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from product.models import Product, Category
from product.views import product
from .models import contact

from .forms import SignUpForm

def frontpage(request):
    # products = Product.objects.all()[0:8]
    products = Product.objects.filter(Trending=True)[0:4]
    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')

def order(request):
    return render(request, 'order/order.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'core/shop.html', context)

def about(request):
    return render(request, 'core/about.html')

def help(request):
    return render(request, 'core/help.html')

def contact2(request):
    return render(request, 'core/contact.html')

def helpshop(request):
    return render(request, 'core/shop.html')

def newcontact(request):
    if request.method == 'POST':
        name = request.POST['contactname']
        email=request.POST['contactemail']
        phone=request.POST['contactphone']
        content=request.POST['contactproblem']
        print(name,email,phone,content)
        Contact=contact(Contname=name,Contactemail=email,Contactphone=phone,Contactreason=content)
        Contact.save()
    return render(request, 'core/contact.html')

