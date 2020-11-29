from django.shortcuts import render,redirect
from django.views import generic,View
from .models import MainTask,SubTask


class IndexView(generic.RedirectView):
    url = '/storys/'


def index(request):
    if request.method == 'GET':
        context = {
            'message':"Hello World",
        }
        return render(request,'app/index.html',context)
        
class StorysView(generic.ListView):
    template_name = "app/storys.html"
    model = MainTask
    context_object_name = "storys"

    def get_queryset(self):
        # return MainTask.objects.order_by('task_seq')
        return MainTask.objects.all()