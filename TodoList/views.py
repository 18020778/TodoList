from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib import messages

def index(request):
    mydictionary = {
        "alltodos": Todo.objects.all().order_by('CreatedAtTime').reverse()
    }
    return render(request,'index.html', context=mydictionary)

@csrf_exempt
def add_todo(request):
    obj = Todo()
    obj.ItemName = request.GET.get('title')
    obj.Description = request.GET.get('description')
    obj.Priority = request.GET.get('priority')
    obj.CreatedAtTime = timezone.now()
    if Todo.objects.filter(ItemName=obj.ItemName).exists():
        messages.error(request,'Title existed') 
    else:
        if (obj.ItemName != None):
            obj.save()
            messages.success(request, "Added Todo in List")
    mydictionary = {
        "alltodos" : Todo.objects.all().order_by('CreatedAtTime').reverse()
    }
    return render(request,'index.html', context=mydictionary)

def delete(request):
    if request.is_ajax and request.method == "POST":
        id = request.POST.get("id", None)
        obj = Todo.objects.get(id = id)
        obj.delete()
        mydictionary = {
            "alltodos": Todo.objects.all().order_by('CreatedAtTime').reverse()
        }
        return render(request, 'index.html', context=mydictionary)

def sortData(request):
    mydictionary = {
        "alltodos": Todo.objects.all().order_by('Priority')
    }
    return render(request,'index.html', context=mydictionary)

def searchData(request):
    text_query = request.GET.get("query")
    mydictionary = {
        "alltodos": Todo.objects.all().filter(ItemName__contains = text_query)
    }
    return render(request, "index.html", context=mydictionary)

def edit(request, id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title": obj.ItemName,
        "description": obj.Description,
        "priority": obj.Priority,
        "id": obj.id
    }
    return render(request, "edit.html", context=mydictionary)

def update(request, id):
    obj = Todo(id=id)
    obj.ItemName = request.GET.get('title')
    obj.Description = request.GET.get('description')
    obj.Priority = request.GET.get('priority')
    import datetime
    update_at = datetime.datetime.now()
    obj.CreatedAtTime = update_at
    if (obj.ItemName != None):
        obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all().order_by('CreatedAtTime').reverse()
    }
    return render(request,'index.html', context=mydictionary)


