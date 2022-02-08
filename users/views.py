from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegisterForm

from djangoVetManagement.decorators import unauthenticated_user

@unauthenticated_user
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)


            if user is not None:

                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Welcome {user.username}')
                return redirect("/")

            else:
                messages.add_message(request, messages.ERROR, 'Invalid input...')
                return render(request, 'login.html', {"form": form}, status=401)

        else:
            messages.add_message(request, messages.ERROR, 'Invalid form...')

    return render(request, "login.html", {"form": form,})


def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         'Logout succesfully')

    return redirect(reverse('login'))


@login_required(login_url="/login/")
def UserRegisterView(request):
    msg_success = None
    msg_fail = None
    success = False
    print(request.user.get_all_permissions())

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            # password2 = form.cleaned_data.get("password2")
            email = form.cleaned_data.get("email")

            user = authenticate(username=username, email = email , password = password1)

            success = True
            msg_success = 'User created.'


            return redirect("home")

        else:
            msg_fail = 'Invalid login input'
    else:
        form = UserRegisterForm()

    return render(request, "register.html", {"form": form, "msg_success": msg_success, "msg_fail": msg_fail, "success": success})