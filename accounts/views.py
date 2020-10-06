from django.shortcuts import render, redirect
from accounts.forms import RegistrationFrom, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required



def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationFrom()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)


def view_profile(request, pk=None):
    #   to view other peoples profiles
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}  # request.user.pk <- to pass primary key
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')  # name of the view is used
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

