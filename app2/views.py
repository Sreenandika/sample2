from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm


# Create your views here.
def dashboard(request):
    profiles=Profile.objects.filter(name='sree')
    return render(request,'dashboard.html',{'profiles':profiles})

def products(request):
    return render(request,'products.html')


def profileadd(request):
   form = ProfileForm(request.POST)
   if form.is_valid():
        form.save()
        return redirect('dashboard')
   return render (request,'profileadd.html', {'form':form})

def profile_list(request):
    profiles=Profile.objects.all()
    return render(request,'profile_list.html',{'profiles':profiles})


def profile_view(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    return render(request,'profile_view.html',{'profile':profile})