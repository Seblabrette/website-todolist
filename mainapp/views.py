from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

from .models import *

# Create your views here.
def homePage(request) :
    context = {}
    return render(request, 'mainapp/homepage.html', context)
    # return HttpResponse("This is the home page")

def userLogin(request) :
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Identifiant ou mot de passe erronés.')

    context = {}
    return render(request, 'mainapp/userlogin.html', context)
    # return HttpResponse("This is the login page")

def userLogout(request):
    logout(request)
    return redirect('homePage')

def userRegister(request) :
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('userLogin')

        context = {'form': form}
        return render(request, 'mainapp/userregister.html', context)

@login_required(login_url='userLogin')
def dashboard(request) :
    lists = ToDoList.objects.filter(user=request.user.id)
    context = {'nblistes':len(lists),'lists':lists}
    return render(request, 'mainapp/dashboard.html', context)
    # return HttpResponse("This is the login page")

@login_required(login_url='userLogin')
def detailView(request, list_id) :
    # msg = 'Detailed view of list #'+str(list_id)+' here'
    # return HttpResponse(msg)
    list = ToDoList.objects.filter(id=list_id)[0]
    itemslist = list.listitem_set.all()
    # print(list)
    # print(itemslist)
    context = {'list':list,'itemslist':itemslist}
    return render(request, 'mainapp/detailview.html', context)

@login_required(login_url='userLogin')
def createlist(request):
    if request.method == 'POST':
        listname = request.POST.get('listname')
        # print('user :', type(request.user))
        # print('title :', listname)
        newlist = ToDoList(user=request.user, title=listname)
        newlist.save()
        return redirect('dashboard')
    context = {}
    return render(request, 'mainapp/createlist.html', context)

def delete_list(request):
    data = json.loads(request.body)
    listId = int(data["listId"])
    list = ToDoList.objects.filter(id=listId)
    list.delete()

    return JsonResponse('List deleted', safe=False)

def rename_list(request, list_id):
    
    if request.method == 'POST':
        listname = request.POST.get('listname')
        list = ToDoList.objects.filter(id=list_id)[0]
        list.title = listname
        list.save()
        return redirect('dashboard')

    list = ToDoList.objects.filter(id=list_id)[0]
    context = {'list':list}
    # print('liste name :', list)
    # msg = 'Rename list #'+str(list_id)+' here' 
    return render(request, 'mainapp/renamelist.html', context)


def delete_item(request):
    data = json.loads(request.body)
    itemId = int(data["itemId"])
    item = ListItem.objects.filter(id=itemId)
    item.delete()

    return JsonResponse('Item deleted', safe=False)

def create_item(request):
    data = json.loads(request.body)
    listId = int(data["listId"])
    list = ToDoList.objects.filter(id=listId)[0]
    texte = data["texte"]
    item = ListItem.objects.create(list=list, description=texte)
    item.save()

    return JsonResponse('Item created', safe=False)

def modify_item(request):
    data = json.loads(request.body)
    itemId = int(data["itemId"])
    action = data["action"]
    value = bool(data["value"])

    item = ListItem.objects.filter(id=itemId)[0]
    
    if action == 'update-complete-status':
        item.completed = value
        item.save()

    return JsonResponse('Item modified', safe=False)
