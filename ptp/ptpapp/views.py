from django.shortcuts import render

from django.shortcuts import render, redirect  
from .forms import StartupsForm  
from .models import Startups  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = StartupsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StartupsForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    startupss = Startups.objects.all()  
    return render(request,"show.html",{'startupss':startupss})  
def edit(request, id):  
    startups = Startups.objects.get(id=id)  
    return render(request,'edit.html', {'startups':startups})  
def update(request, id):  
    startups = Startups.objects.get(id=id)  
    form = StartupsForm(request.POST, instance = startups)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'startups': startups})  
def destroy(request, id):  
    startups = Startups.objects.get(id=id)  
    startups.delete()  
    return redirect("/show")  