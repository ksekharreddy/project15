from django.shortcuts import render

# Create your views here.
def app3 (request):
    d={'Domain':'python','Batch':2}
    return render (request,'app3.html',context=d)
