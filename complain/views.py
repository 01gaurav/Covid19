from django.shortcuts import render
from .forms import OurInformer
# Create your views here.
from .models import storecomplain
from django.http import  *


def formslev1(request):
    if request.method == 'POST' :
        form=OurInformer(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/complain/')

    else:
        form = OurInformer()

    return render(request,'fillcomplains.html',{'form':form})
