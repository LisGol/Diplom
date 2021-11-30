from django.contrib.auth import (
    get_user_model,
    authenticate,
    login as login_user,
    logout as logout_user,
)
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from user.autontification.forms import RegistrationForm, LoginForm
#from diplomaproject import settings


User = get_user_model()


def registration(request):
    if request.user.is_authenticated:
        redirect(reverse(('Home')))
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form['password2'])
            user.save()
            return redirect(reverse('Home'))
    else:
        form = RegistrationForm()
    return render(
        request,
        'diplom/autontification/auth.html',
        {'form': form}
    )


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('Home'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                redirect_url= request.GET.get('next',reverse('Home')
                )
                login_user(request, user)
                return redirect(reverse('home'))
        else:
            form = LoginForm()
            next_url = request.GET.get('next', '')
        return render(
            request,
            'diplom/autontification/login.html',
            {'form': form, 'next': next_url}
            )

def logout(request):
    logout_user(request)
    return redirect(reverse('home'))
