from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import ProductForm, CategoryForm

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Django !!!</h1>")


def index2(request):
    return render(request,'index.html')

def register(request):
    # every form handling would have 2 reuests: 1. GET reuest load the empty form 
              # 2. form submission by using POST 
    if request.method == "GET":
        return render(request,'register.html')
    else:
        # capture the values enterd by user
        u = request.POST['username']
        p = request.POST['password']
        cp = request.POST['confirm_password']
        # insert the user details in db
        # user = User.objects.create(username =u, password=p)
        # user.save()
        user = User.objects.create(username=u)
        user.set_password(p) #encryption
        user.save()
        return render(request,'index.html')
    
def signup(request):
    if request.method=="GET":
        f = UserCreationForm()
        context = {'form':f}
        return render(request,'signup.html',context)    
    else:
        context={}
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context['success']="Registered Successfully!!"
            return render(request,'index.html',context)
        else:
            context['error']="Please enter the valid details"
            return render(request,'signup.html',context)
        
def addCategory(request):
    if request.method=="GET":
        f = CategoryForm()
        context={'form':f}
        return render(request,'addcat.html', context)
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'index.html')
    
def addProduct(request):
    if request.method=="GET":
        f = ProductForm()
        context={'form':f}
        return render(request,'addproduct.html', context)
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'index.html')



