from Tools.scripts.make_ctype import method
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Detailview(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task'
# Create your views here.
class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'updatenew.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('taskname','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
# def detail(request):
#     task=Task.objects.all()
#     return render (request,'detail.html',{'task':task})
def delete(request,task_id):
    task2 = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task2.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task})