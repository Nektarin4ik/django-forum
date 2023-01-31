from django.shortcuts import render
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import User, CommentsAnime
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import UserRegistrationForm, UserProfileForm, UserLoginForm, CommentFormAnime
# Create your views here.


class UserRegistrationView(CreateView):

    model = User
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('basepage:index')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class LoginProfileView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm


class logout(View):

    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('basepage:index'))
