from django.shortcuts import render

# Create your views here.
def app4 (request):
    d={'name':'sekhar reddy','number':7702639569}
    return render (request,'app4.html',context=d)
