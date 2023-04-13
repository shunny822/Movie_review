from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm,CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/signup.html',context)


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
    }

    return render(request,'accounts/update.html',context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('reviews:index')


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('reviews:index')


def detail(request,account_pk):
    account = get_user_model().objects.get(pk=account_pk)
    reviews = account.review_set.all()
    context = {
        'account': account,
        'reviews': reviews,
    }
    return render(request,'accounts/detail.html',context)


def password_change(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('reviews:index')

    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/password_change.html',context)