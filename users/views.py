from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm, ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.urls import path 
from mainapp.models import Category
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has now been created')
            #Register completion
            return redirect('login')
            #Redirects to login page
            
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    categories=Category.objects.all()
    if request.method=='POST':
        p_form=ProfileUpdateForm(request.POST, request.FILES,instance=request.user.userprofile) 
        u_form=UserUpdateForm(request.POST,instance=request.user.userprofile)
        #Both forms hold different data, one for profile pic, the other for users fav cats
        if p_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        p_form=ProfileUpdateForm(instance=request.user.userprofile)
        u_form=UserUpdateForm(instance=request.user.userprofile)  
    return render(request, 'users/profile.html',{
        'cats':categories,
        'p_form':p_form,
        'u_form':u_form
    })