from .models import User
from django.shortcuts import render
from django.contrib import auth
from django.core.mail.message import EmailMessage
# Create your views here.

# 회원 가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'], vegan=request.POST['vegan'])

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

def reset_password(request):
    return render(request, 'reset_password.html')

def index(request):
    return render(request, 'index.html')

def send_email(request):
    subject = "message"
    to = ["yukmj1123@gmail.com"]
    from_email = "veganiateam@gmail.com"
    message = "메시지 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
