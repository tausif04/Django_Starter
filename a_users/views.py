from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile':profile})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instyance=request.user.profile )
    return render(request, 'a_users/profile_edit.html', {'form':form})
