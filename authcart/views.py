from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            # return HttpResponse("password is incorrect")
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')                   
        try:
            if User.objects.get(username=email):
                # return HttpResponse("Email already Exist ")
                # return HttpResponse("email already exist")
                messages.info(request,"Email is Taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        # user.is_active=False
        user.save()
        # return HttpResponse("User is created", email)

        # email_subject="Activate Your Account"
        # message=render_to_string('activate.html',{
        #     'user':user,
        #     'domain':'127.0.0.1:8000',
        #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token':generate_token.make_token(user)

        # })
        # return HttpResponse("User is created", email)
        messages.info(request, " Account is Created Successfully")
        return redirect("/auth/login/")
        
    return render(request, "signup.html")

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username, password=userpassword)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            # return render(request, 'index.html')
            return redirect('/')
        else:
            messages.error(request,"InvalID Credentials")
            return redirect('/auth/login')
        

    return render(request, "login.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')
