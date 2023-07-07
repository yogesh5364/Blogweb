from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignupForm
from .models import AddUser
from django.views import View
from django.core.mail import send_mail 
from django.conf import settings
from random import randint
# . --> pwd

# Create your views here.
def index(request):
    if request.session.get("islogin"):
        return render(request, "afterlogin.html")
    return render(request, 'blog.html')
# templates --> index.html
def login(request):
    if request.session.get('islogin'):
        return render(request, "afterlogin.html")
    else:
        form = LoginForm()
        return render(request, 'blog_login.html', {'form': form})

def signup(request):
    form = SignupForm()
    return render(request, 'blog_signup.html', {'form': form})

def aftersignup(request):
    if request.method == "GET":
        return redirect('/blog_signup/')
    else:
        # To get data from html file 
        # email = request.POST.get('email')
        # pass_ = request.POST.get('password') 
        # to get data from django form use the following
        form = SignupForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            passwd = form.cleaned_data['password']
            try:
                obj = AddUser.objects.get(email=email)
            except Exception:
                up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                lw = "abcdefghijklmnopqrstuvwxyz"
                sp = "~!@#$%^&*()_{}[]:<>?/\|"
                ds = "0123456789"

                rules = [ 
                            len(passwd) >= 8 ,
                            any([(i in up) for i in passwd]),
                            any([(i in lw) for i in passwd]),
                            any([(i in sp) for i in passwd]),
                            any([(i in ds) for i in passwd]),
                            all([(i != '') for i in passwd]) 
                        ]
                if all(rules):
                    AddUser.objects.create(firstname=fname, lastname=lname,
                    email=email, password=passwd)
                    # return HttpResponse(f"{fname}, {email}")
                    form = LoginForm()
                    return render(request, 'blog_login.html', {'form': form})
                else:
                    msg = "Password is Invalid"
                    form = SignupForm()
                    return render(request, 'blog_signup.html', {'form': form, 'msg': msg})              
            else:
                msg = "User Already Exists"
                form = SignupForm()
                return render(request, 'blog_signup.html', {'form': form, 'msg': msg})
        else:
            msg = "Form Is Invalid"
            form = SignupForm()
            return render(request, 'blog_signup.html', {'msg': msg, 'form': form})

class afterlogin(View):
    def get(self, request):
        return redirect("/blog_login/")

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = AddUser.objects.get(email=email)
            except Exception:
                msg = "Email is Invalid"
                form = LoginForm()
                return render(request, "blog_login.html", {'form': form, 'msg': msg})
            else:
                if password == user.password:
                    request.session['email'] = email 
                    request.session['islogin'] = "true"
                    return render(request, "afterlogin.html")
                else:
                    msg = "Password is Invalid"
                    form = LoginForm()
                    return render(request, "blog_login.html", {'form': form, 'msg': msg})

def logout(request):
    del request.session['email']
    del request.session['islogin']
    return redirect("/")

def forgot(request):
    return render(request, "forgot.html")

class Getemail(View):
    def get(self, request):
        msg = "Invalid Method"
        return render('forgot.html', {'msg': msg})
    
    def post(self, request):
        email = request.POST.get('email')
        try:
            user = AddUser.objects.get(email=email)
        except Exception:
            msg = "Email is Invalid"
            form = LoginForm()
            return render(request, "blog_login.html", {'form': form, 'msg': msg})
        else:
            from_email = settings.EMAIL_HOST_USER
            otp = randint(1111, 9999)
            message = f"OTP for forgot password is {otp}"
            subject = "OTP FOR CHANGE PASSWORD"
            try:
                send_mail(subject, message, from_email, [email], auth_password=settings.EMAIL_HOST_PASSWORD)
            except Exception as err:
                return HttpResponse(err)
            else:
                msg = 'Please Check Your Mail For OTP'
                request.session['otp'] = otp 
                request.session['email'] = email 
                return render(request, "getotp.html", {'msg': msg})

class Checkotp(View):
    def get(self, request):
        msg = "Invalid Method"
        del request.session['otp']
        return render('forgot.html', {'msg': msg})
    
    def post(self, request):
        otp = request.POST.get('otp')
        otp1 = str(request.session.get('otp'))
        if otp == otp1:
            del request.session['otp']
            return render(request, "newpassword.html") 
        else:
            del request.session['otp']
            msg = "INCORRECT OTP"
            form = LoginForm()
            return render(request, "blog_login.html", {'msg': msg, 'form': form})

class Changepass(View):
    def get(self, request):
        msg = "Invalid Method"
        del request.session['email']
        return render('forgot.html', {'msg': msg})
    
    def post(self, request):
        passwd = request.POST.get("newpass")
        user = AddUser.objects.get(email = request.session['email'])

        up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lw = "abcdefghijklmnopqrstuvwxyz"
        sp = "~!@#$%^&*()_{}[]:<>?/\|"
        ds = "0123456789"

        rules = [ 
                    len(passwd) >= 8 ,
                    any([(i in up) for i in passwd]),
                    any([(i in lw) for i in passwd]),
                    any([(i in sp) for i in passwd]),
                    any([(i in ds) for i in passwd]),
                    all([(i != '') for i in passwd]) 
                ]
        if all(rules):
            user.password = passwd 
            user.save()
            msg = 'Login With New Password'
            del request.session['email']
            form = LoginForm()
            return render(request, "blog_login.html", {'form': form, 'msg': msg})
        else:
            msg = "Password is Invalid"
            return render(request, 'newpassword.html', {'msg': msg})

def about(request):
    return render(request, "blog_about.html")