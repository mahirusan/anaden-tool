from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method == 'GET':
        context = {
            'message':"Hello World",
        }
        return render(request,'app/index.html',context)
        
