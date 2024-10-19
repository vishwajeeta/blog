from django.shortcuts import render
from .models import sample
# Create your views here.
def home(request):
    data=sample.objects.all()
    return render(request,'index.html',{'data':data})