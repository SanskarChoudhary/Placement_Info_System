from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import userRegistrationForm,userProfileUpdateForm,userUpdateForm
from django.contrib.auth.decorators import login_required

def register(req):
    if req.method=='POST':
        form=userRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(req,'Your account has been created, You can login now')
            return redirect('login')
    else:
        form=userRegistrationForm()
    return render(req,'users/register.html',{'form':form})

@login_required
def profile(req):
    if req.method=='POST':
        u_form=userUpdateForm(req.POST,instance=req.user)
        p_form=userProfileUpdateForm(req.POST,req.FILES,instance=req.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(req,'Your Profile has been updated')
            redirect('profile')
    else:
        u_form=userUpdateForm(instance=req.user)
        p_form=userProfileUpdateForm(instance=req.user.profile)
    context={'u_form':u_form,'p_form':p_form,'title':'Profile'}
    return render(req,'users/profile.html',context)