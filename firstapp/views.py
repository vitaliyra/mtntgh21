from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Hit

 
def index(request):
    tom = Hit.objects.get(id=1)
    tom.hit_count+=1
    tom.save()

    data = {"header": tom.hit_count}
    return render(request, "index.html", context=data)