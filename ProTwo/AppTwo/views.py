from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import UserForm,UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    user_listing = User.objects.order_by("email")
    user_dict = {"users":user_listing,"insert_me":"Kindly, go to /users to Sign Up!",'text':'hello world','number':100}
    return render(request,"AppTwo/index.html",user_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def show_user(request):
    user_listing = User.objects.order_by("email")
    user_dict = {"users":user_listing}
    return render(request,"AppTwo/show_users.html",user_dict)

def help(request):
    my_dict = {'help':'Hello, this is from AppTwo/views.py file'}
    return render(request,'AppTwo/help.html',context=my_dict)

def user(request):
    registered = False
    # form = UserForm()
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return index(request)
        else:
            print(user_form.errors,profile_form.errors)
    else:
        # print("Error, form invalid!!")
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,"AppTwo/users.html",
                                            {"user_form":user_form,
                                            "profile_form":profile_form,
                                            'registered':registered}
                                            )

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed!!")
            print("Username: {}, Password: {}".format(username,password))
            return HttpResponse("Invalid login details.")
    else:
        return render(request,'AppTwo/login.html')
