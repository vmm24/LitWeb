from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account successfully created!')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request,'Account successfully updated!')
            return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
    context = {
        'update_form': update_form
    }

    return render(request, 'users/profile.html', context)
