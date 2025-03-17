from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from product.models import (
    UserProfile,
    Item
)
from django.contrib import messages
from .forms import *


def index(request):
    hot = Item.objects.all()[:24]
    context = {
        'hot': hot
    }
    return render(request, 'landing/index.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usr = User.objects.get(username=form.cleaned_data['username'])
            UserProfile.objects.create(user=usr)
            messages.success(request, 'Your Account Was Created Sucessfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, 'auth/register.html', context)


@login_required
def logoutView(request):
    logout(request)
    messages.info(request, "Your Session Has Ended!")
    return redirect('logoutPage')


def logoutPage(request):
    return render(request, 'auth/logout.html', context={})
