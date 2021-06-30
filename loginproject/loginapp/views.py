from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# 회원 가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            auth.login(request, user)
            #회원가입 성공페이지
            return render(request, 'success.html')
    return render(request, 'signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        
        user = auth.authenticate(request, username=username, password=password)
        
        
        if user is not None:
            auth.login(request, user)
            #로그인 성공시 메인화면
            return render('/')

        else:

            return render(request, 'fail.html')

    else:
        return render(request, 'login.html')

# 로그 아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        #로그아웃 성공화면=메인화면
        return render('/')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')