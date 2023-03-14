from django.shortcuts import render

# Create your views here.
def jinga_app2 (request):
    d={'adress':'Bangloore','mobnum':7702639569}
    return render (request,'jinga.app2.html',context=d)
