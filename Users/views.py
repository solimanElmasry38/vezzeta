from django.shortcuts import render
from django.shortcuts import redirect
from .filters import SearchFilter
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as signIn
from django.contrib.auth import logout as signOut
from django.contrib.auth import authenticate

# Create your views here.

def home(request):

    Searchfield = SearchFilter()
    cond = request.user.is_authenticated

    context = {'Searchfield': Searchfield, "cond": cond,}

    return render(request, 'pages/home.html', context)

def signUp(request):
    Searchfield = SearchFilter()

    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        allow = authenticate(request, username=username, password=password)
        if allow is not None:
            signIn(request, allow)
            return redirect('/creates/')


    cond = request.user.is_authenticated
    context = {'signform': form, 'Searchfield': Searchfield, "cond": cond,}
    return render(request, 'pages/sign_up.html', context)

def logIn(request):
    Searchfield = SearchFilter()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        allow = authenticate(request, username=username, password=password)
        if allow is not None:
            signIn(request, allow)
            return redirect('/')

    cond = request.user.is_authenticated
    context = {'Searchfield': Searchfield, "cond": cond,}
    return render(request, 'pages/log_in.html', context)

def logOut(request):

    signOut(request)
    return redirect('/login/')

def Adds(request):
    Searchfield = SearchFilter()
    cond = request.user.is_authenticated

    context = {'Searchfield': Searchfield, "cond": cond,}

    return render(request, 'pages/Adds.html', context)

def EditeUserInfo(request):
    Searchfield = SearchFilter()
    cond = request.user.is_authenticated

    currentProfile = Profile.objects.get(user=request.user)
    euif = EditeUserInfoForm
    epif = EditeProfileInfoForm

    if request.method == 'POST':
        UserInfo = EditeUserInfoForm(request.POST, instance=request.user)
        ProfileInfo = EditeProfileInfoForm(
            request.POST, instance=currentProfile)
        if UserInfo.is_valid() and ProfileInfo.is_valid():
            UserInfo.save()

            myPorf = ProfileInfo.save(commit=False)
            myPorf.user = request.user

            myPorf.save()

    x = EditeUserInfoForm(instance=request.user)

    y = EditeProfileInfoForm(instance=currentProfile)

    context = {'Searchfield': Searchfield, "cond": cond,'euif': x, 'epif': y, }
    return render(request, 'pages/EditeUserInfo.html', context)

def CreateProfile(request):
    Searchfield = SearchFilter()
    cond = request.user.is_authenticated


    currentProfile = Profile.objects.get(user=request.user)
    euif = EditeUserInfoForm
    epif = EditeProfileInfoForm

    if request.method == 'POST':
        ProfileInfo = EditeProfileInfoForm(
            request.POST, instance=currentProfile)
        if ProfileInfo.is_valid():

            myPorf = ProfileInfo.save(commit=False)
            myPorf.user = request.user

            myPorf.save()
            return redirect('/')



    y = EditeProfileInfoForm(instance=currentProfile)
    y.phone = 101357237
    cond = request.user.is_authenticated
    context = {'Searchfield': Searchfield, "cond": cond, 'epif': y, 'cond':cond ,}
    return render(request, 'pages/CreateProfile.html', context)

def profile(request):

    myprofile = Profile.objects.get(user= request.user )
    user = request.user

    




    Searchfield = SearchFilter()
    cond = request.user.is_authenticated

    context = {'Searchfield': Searchfield, "cond": cond,'myprofile':myprofile,'user':user,}

    return render(request, 'pages/profile.html', context)