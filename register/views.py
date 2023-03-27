from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from register import forms
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# VIEW PURPOSE: Allow The User To Create An Account With No Privileges. The User Will Be Saved Into The Database.
def registerPage(response):
    form = forms.RegisterForm() # REGISTERFORM: Create RegisterForm() Instance Found In "forms" And Store It In A Variable. RegisterForm() Extends The 'UserCreationForm'.

    if response.method == "POST": # POST REQUEST: Checks If A 'POST' Request Is Made. Whether The Submit Button Is Pressed In The Form.
        form = forms.RegisterForm(response.POST) # SAVE FORM: Store The Values Within The Form In A Variable If Button Is Pressed.

        if form.is_valid(): # IF STATEMENT: Check If The Form Is Valid. If The Form Has No Errors It Is Valid.
            form.save()  # SAVE: If The Form Is Valid Save The User Into The Database.
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            message = "Welcome To The Expense Tracker App.\n\nYou have successfully created an account.\n\nUSERNAME: {}.".format(username)
            send_mail("Welcome To The Expense Tracker App!", message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

            return HttpResponseRedirect("/add")  # REDIRECT: Redirect To The Home Page Once The User Has Been Saved.
        else:
            messages.warning(response, "Invalid Form")  # ELSE: The Form Is Invalid Display A Message On The Web Page.

    return render(response, "register/register.html", {"form": form}) # RENDER: Display Page With Form Passed In.

# VIEW PURPOSE: Display A Logout Screen If The User Has Logged Out. If The User Isn't Logged In And They Go To '/logout' They Go To The Welcome Screen.
def logoutPage(response):
    user = response.user  # CURRENT USER: Store The Current User In A Variable.

    # IF STATEMENT: If The User Is Anonymous. This Is To Say Not Logged In.
    if str(user) == "AnonymousUser":
        return HttpResponseRedirect("/")  # REDIRECT: Go To The Welcome Screen.
    else:
        firstname = user.first_name # ELSE: Get The Users First Name.
        context = {"firstName": firstname} # CONTEXT: Store Their First Name In A Dictionary So That It Can Be Passed Into The Logout Template To Be Displayed.
        logout(response) # LOGOUT: Logout The User From The System

    return render(response, "register/logout.html", context) # RENDER: Display Page With Passed In Dictionary.
