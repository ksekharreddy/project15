from django.shortcuts import render

# Create your views here.
def apptwo (request):
    d={'name':'sekhar','age':21}
    return render ( request,'apptwo.html',context=d)