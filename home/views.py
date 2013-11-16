# Create your views here.
from django.shortcuts import   *
from django.http import HttpResponse
from home.models import *
import random,datetime
def index(request):
    class_list=[]

    if request.GET.has_key("c"):
        reponse=render_to_response("index.html")
        reponse.delete_cookie("username")
        return reponse
    if not request.COOKIES.has_key("username"):
        return render_to_response("index.html")
    else:
        attendenced=False
        username=request.COOKIES.get("username")
        invate_key=Student.objects.get(username=username).invate_key
        classname=Student.objects.get(username=username).className
        user_list=Attendence.objects.filter(date=datetime.date.today(),username=username)
        if user_list:
            attendenced=True
#attendence
        if request.GET.has_key("a"):
            if not attendenced:
                a=Attendence()
                a.username=username
                a.date=datetime.date.today()
                a.time=datetime.datetime.now().strftime("%H:%M")
                a.className=Student.objects.get(username=username).className
                a.save()
                attendenced=True
#check if is admin
        if classname=="admins":
            object_list=AddClass.objects.order_by("-id")
            for i in object_list:
                 class_list.append(i.className)


        return render_to_response("index.html",{"username":username,"invate_key":invate_key,"attendenced":attendenced,"class_list":class_list})
def login(request):
    error=False
    if not request.POST:
        return  render_to_response("login.html",{"error":error})
    username=request.POST["username"]
    password=request.POST["password"]
    user_list=Student.objects.filter(username=username,password=password)
    if not user_list:
        error=True
        return  render_to_response("login.html",{"error":error})
    username=user_list[0].username
    response=render_to_response("login.html",{"username":username})
    response.set_cookie("username",username)
    return  response
def register(request):
    status="fail"
    if not request.POST:
        return  render_to_response("register.html",{"status":status})
    else:
        username=request.POST["user"]
        passwd=request.POST["passwd"]
        invated_key=request.POST["invated"]
        if Student.objects.filter(username=username):
            userFailed=True
            return render_to_response("register.html",{"status":status,"userFailed":userFailed})
        elif not AddClass.objects.filter(invate_key=invated_key,canRegister=True):
            invatedFailed=True
            return render_to_response("register.html",{"status":status,"invatedFailed":invatedFailed})
        className=AddClass.objects.get(invate_key=invated_key).className
        Student.objects.create(username=username,password=passwd,className=className,invate_key=invated_key)
        status="success"
        return  render_to_response("register.html",{"status":status})
def draw(request):
    maps={}
    if not request.GET:
        return HttpResponse("hey guy,go to bed!")


    if request.GET.has_key("c"):
        classname=request.GET["c"]
        today=datetime.date.today()
        total=Student.objects.filter(className=classname).__len__()
        attendenced=Attendence.objects.filter(className=classname,date=today).__len__()
        noattendenced=total-attendenced
        
        stu_list=Student.objects.filter(className=classname)
        for stu in stu_list:
            obj_set=Attendence.objects.filter(username=stu,date=today)
            if obj_set:
                maps[stu]="YES"
            else:
                maps[stu]="NO"




    return render_to_response("draw.html",{'total':total,'attendenced':attendenced,'noattendenced':noattendenced,'maps':maps})
