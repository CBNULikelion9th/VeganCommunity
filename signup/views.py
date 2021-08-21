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
        print(user)
        
        if user is not None:
            auth.login(request, user)
            #로그인 성공시 메인화면
            return render(request, 'loginsucess.html')

        else:

            return render(request, 'fail.html')

    else:
        return render(request, 'login.html')

# 로그 아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        #로그아웃 성공화면=메인화면
        return render(request, 'index.html')

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def index(request):
    return render(request, 'index.html')

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)

class UserPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html' #템플릿을 변경하려면 이와같은 형식으로 입력
    success_url = 'password_reset_done'
    form_class = PasswordResetForm
    
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            return render(self.request, 'password_reset_done_fail.html')
            
class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html' #템플릿을 변경하려면 이와같은 형식으로 입력


