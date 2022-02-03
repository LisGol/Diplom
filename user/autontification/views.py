from urllib import request

from django.contrib.auth import (
    get_user_model,
    authenticate,
    login as login_user,
    logout as logout_user,
)
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView

from user.autontification.forms import RegistrationForm, LoginForm

# from diplomaproject import settings


User = get_user_model()

def logout(request):
    logout_user(request)
    return redirect(reverse('home'))


def registration(request):
    if request.user.is_autontification:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()
            return redirect(reverse('home'))
    else:
        form = RegistrationForm()
    return render(
        request,
        'diplom/autontification/auth.html',
        {'form': form}
    )


def login(request):
    if request.user.is_autontification:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['email_or_username'],
                email=form.cleaned_data['email_or_username'],
                password=form.cleaned_data['password']
            )
            if user:
                redirect_url = request.GET.get('next') or reverse('home')
                login_user(request, user)
                return redirect(redirect_url)
    else:
        form = LoginForm()
    next_url = request.GET.get('next', '')
    return render(
        request,
        'diplom/autontification/login.html',
        {'form': form, 'next': next_url}
    )

    # class ShowProfilePageView(DetailView):
    #     model = Profile
    #     template_name = 'diplom/autontification/profal.html'
    #
    #     def get_context_data(self, *args, **kwargs):
    #         users = Profile.objects.all()
    #         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
    #         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
    #         context['page_user'] = page_user
    #         return context
    #
    # class CreateProfilePageView(CreateView):
    #     model = Profile
    #
    #     template_name = 'diplom/autontification/create_profile.html'
    #     fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']
    #
    #     def form_valid(self, form):
    #         form.instance.user = self.request.user
    #         return super().form_valid(form)
    #
    #     success_url = reverse_lazy('tasks')
    #
    #     from django.contrib.auth import (
    #         get_user_model,
    #         authenticate,
    #         login as login_user,
    #         logout as logout_user
    #     )