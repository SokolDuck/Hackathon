from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import views
from django.urls import reverse_lazy


class RegisterView(views.View):
    def get(self, request):
        form = UserCreationForm()
        args = {'form': form}

        return render(request, 'register.html', args)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(
                request,
                username=username,
                password=password
            )

            return redirect('/')


class LoginView(views.View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'login.html')

    def post(self, request):
        args = {}

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            args = {'username': username}
            print(user)
            if username == 'admin':
                print(1)
                return redirect('/admin/')
            else:
                print(2)
                return redirect('/')

        else:
            args['login_error'] = 'User not found'

        return redirect('/')


class LogoutView(views.View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')
