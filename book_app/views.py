from django.http import HttpResponse
from django.shortcuts import render
from .models import UserModel

# Create your views here.
def home_page(request):
    return render(request,"home.html")
def profile_page(request,):
    return render(request,"profile.html",{"name":"amit","email":"amit@gmail.com","role":"admin","user_data":[
        {"name":"lulu","email":"lulu@gmail.com"},
        {"name": "chuchu", "email": "chuchu@gmail.com"},
        {"name": "coco", "email": "coco@gmail.com"}


    ]})
def contact_page(request):
    return render(request,"contact.html",{"range":range(0,10)})



def marks_page(request):
    return render(request,"marks.html",{"marks":20,"role":"marks"})


def add_user(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        print(name,email)
        data=UserModel.objects.create(
            name=name,
            email=email
        )
        return HttpResponse("User Added")
    return render(request,"user_form.html")


