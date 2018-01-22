import hashlib

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from one.models import User, Movie


def home(request):
    return render(request,'one/home.html')

def home_logined(request):
    username = request.session.get('username')
    usericon = User.objects.filter(u_name=username).last().u_icon
    movies=Movie.objects.all()
    context={
        'username':username,
        'usericon':usericon,
        'movies':movies
    }
    return render(request, 'one/home_logined.html',context)

def wodesc(request):
    username = request.session.get('username')
    user = User.objects.filter(u_name=username).last()
    movieid = request.GET.get('movieid')

    movie = Movie.objects.filter(pk=movieid).last()
    movieidlist = user.movie_set.all().values('id')
    for i in movieidlist:
        if i['id'] == int(movieid):
            return JsonResponse({'msg': 'no'})

    user.movie_set.add(movie)
    return JsonResponse({'msg': 'ok'})


def home_logined_collected(request):
    username = request.session.get('username')
    usericon = User.objects.filter(u_name=username).last().u_icon
    user = User.objects.filter(u_name=username).last()

    allmovie = user.movie_set.all()

    context = {
        'username':username,
        'usericon':usericon,
        'allmovie': allmovie,
    }

    return render(request,'one/home_logined_collected.html',context)

def delwodesc(request):
    username = request.session.get('username')
    user = User.objects.filter(u_name=username).last()

    movieid = request.GET.get('movieid')

    movie=Movie.objects.filter(id=movieid).last()

    movie.id_user.remove(user)

    return JsonResponse({'msg':'ok'})

def login(request):
    return render(request,'one/login.html')

def dologin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.filter(u_name=username)
    if len(user) > 0:
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        newpassword = md5.hexdigest()
        if newpassword == user.first().u_password:
            request.session['username'] = username
            response = HttpResponseRedirect(reverse('one:homelogin'))
            return response
        else:
            return HttpResponse('密码错误')
    else:
        print('您输入的账号不存在')
        return redirect(reverse('one:login'))

def register(request):
    return render(request, 'one/register.html')

def doregister(request):
    try:
        username=request.POST.get('username')
        password=request.POST.get('password1')
        print(password)
        print(password)
        print(password)
        print(password)
        email=request.POST.get('email')
        usericon=request.FILES['usericon']

        md5=hashlib.md5()
        md5.update(password.encode('utf-8'))
        p=md5.hexdigest()
        password=p
        print(password)
        print(password)
        user=User()
        user.u_name=username
        user.u_password=password
        user.u_email=email
        user.u_icon=usericon
        user.save()

        request.session['username']=username
        return redirect(reverse('one:homelogin'))
    except Exception as e:
        print('注册失败')
        return HttpResponse('注册失败')

def jianceuser(request):
    uname=request.GET.get('uname')
    user = User.objects.filter(u_name=uname)
    if len(user)>0:
        msg='用户名存在'
        state=201
    else:
        msg='不存在'
        state = 200
    data={
        'msg':msg,
        'state':state,
    }
    return JsonResponse(data)

def userinfo_mod(request):
    username = request.session.get('username')
    usericon = User.objects.filter(u_name=username).last().u_icon
    context = {
        'username': username,
        'usericon': usericon,
    }
    return render(request,'one/userinfo_mod.html',context)

def douserinfo_mod(request):
    username = request.session.get('username')
    user = User.objects.filter(u_name=username)
    if len(user)>0:
        user=user.last()
        user_email=request.POST.get('useremail')
        print(user_email)
        print(user_email)
        print(user_email)
        print(user_email)
        usericon = request.FILES['u_icon']
        print(usericon)
        print(usericon)
        print(usericon)
        print(usericon)
        print(usericon)
        user.u_email=user_email
        user.u_icon=usericon
        user.save()
    return HttpResponseRedirect(reverse('one:homelogin'))