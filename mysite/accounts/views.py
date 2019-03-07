from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import EditProfileForm, AvatarForm, SkillForm, SignUpForm

from projects.models import Project


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "That user account has been disabled." )
            else:
                messages.error(request, "Username or password is incorrect.")
    return render(request, 'login.html', {'form': form})


def my_profile(request):
    """Shows the users profile, shows users projects and skills"""
    profile = Profile.objects.get(user=request.user)
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'profile.html', {'profile': profile, 'projects': projects})


@login_required
def edit_profile(request):
    """Allows user to edit their email or name"""
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


@login_required
def change_password(request):
    """Allows user to change their password"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/accounts/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def change_avatar(request):
    """Allows user to upload and save a avatar"""
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = AvatarForm()
    return render(request, 'change_avatar.html', {
        'form': form
    })


@login_required
def change_skills(request):
    """Allows user to select their skills from a drop down menu"""
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = SkillForm()
    return render(request, 'skills.html', {
        'form': form
    })







