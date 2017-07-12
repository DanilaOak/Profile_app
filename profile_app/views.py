from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def home(request):
    return render(request, 'profile_app/home.html', {})


def signin(request):
    return render(request, 'profile_app/signin.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signin')
    else:
        form = UserForm()
    return render(request, 'profile_app/signup.html', {'form': form})


@login_required()
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'profile_app/profile_edit.html', {'form': form, "object": request.user})
