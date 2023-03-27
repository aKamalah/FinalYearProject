from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from main import forms
from .models import IncomeExpense
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .filters import FilterIncomeExpense
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# VIEWS: Functions That Takes HTTP Requests And Returns HTTP Response, Like HTML Documents (Web Pages).
# TEMPLATES: Create Templates Folder In Application Folder. Within Folder Create A Folder Named After The Application. Templates Stored And Accessed Here.
# RETURN RENDER: return render(response, template, context).
# RETURN RENDER - RESPONSE: Request.
# RETURN RENDER - TEMPLATE: .html Website To Be Displayed.
# RETURN RENDER - CONTEXT: Dictionary To Be Passed Into The Template So That Values Can Be Accessed And Used.

# VIEW PURPOSE: Render Out A Welcome Page For Unauthenticated Users.
def welcomePage(response):
    if not response.user.is_authenticated: # IF STATEMENT: Checks Whether The User Is Authenticated. This Is To Say Logged In.
        context = {}
        return render(response, "main/welcomePage.html", context) # RENDER: Render 'welcomePage.html' If The User Is Not Authenticated.
    else:
        return HttpResponseRedirect("/home") # REDIRECT: If The User Is Authenticated Redirect To The Home Page.

# VIEW PURPOSE: Dashboard For The User. They Can See Their Income And Expense Totals, And A Diagram To Reflect This.
def homePage(response):
    items = IncomeExpense.objects.filter(user = response.user) # OBJECTS: Get All Income/Expenses Objects A User Has Made And Store In A QuerySet.

    income = 0 # INCOME RUNNING TOTAL: Running Total For Income.
    expense = 0 # EXPENSE RUNNING TOTAL: Running Total For Expenses.

    for item in items: # FOR LOOP: Loop For The Amount Of Objects In The QuerySet.
        if item.typeIE == "INCOME": # IF STATEMENT: For The Current Object In The QuerySet Check If It Is "INCOME".
            income = income + item.value # INCOME RUNNING TOTAL: Increase The Running Total for 'income' If It Is Based Off Object Value.
        else:
            expense = expense + item.value # EXPENSE RUNNING TOTAL: Else Increase The Running Total for 'expense'.

    # IF STATEMENT: Statement Below Deduces What Colour Overall Balance Should Be.
    overall = income-expense
    if overall == 0:
        overallColour = "WHITE"
    elif overall > 0:
        overallColour = "GREEN"
    else:
        overallColour = "RED"

    context = {"income": income, "expense": expense, "overall": overall, "overallColour": overallColour}
    return render(response, "main/homePage.html", context)

# VIEW PURPOSE: Allow The User To Add An Income/Expense By Completing And Submitting A Form.
def addPage(response):
    if response.user.is_authenticated: # USER AUTHENTICATED: Checks Whether The User Is Authenticated. This Is To Say Logged In.

        if response.method == "POST": # IF STATEMENT: Check If A 'POST' Request Is Made. Whether Submit Button Is Pressed In The Form.
            form = forms.AddIncomeExpense(response.POST) # FORM: Get Data From The Submitted Form And Store It In A Variable.

            if form.is_valid(): # IS_VALID(): Check If The Form Is Valid. If The Form Has No Errors It Is Valid.
                typeIE = form.cleaned_data["typeIE"] # CLEAN DATA: Get Income/Expense Choice Input And Store In A Variable.
                description = form.cleaned_data["description"] # CLEAN DATA: Get Description Input And Store In A Variable.
                value = form.cleaned_data["value"] # CLEAN DATA: Get Value Input And Store In A Variable.
                value = round(value, 2) # CLEAN DATA: Ensures The Value Passed In Is Rounded To 2.D.P.
                date = form.cleaned_data["date"] # CLEAN DATA: Get Date Input And Store In A Variable.

                obj = IncomeExpense(user = response.user, typeIE = typeIE, description = description, value = value, date = date)  # CREATE OBJECT: Create 'IncomeExpense' Object Using The Form Values.
                obj.save() # SAVE OBJECT: Save Object Into The Database.
                messages.success(response, "You Have Successfully Added " + obj.description)  # DISPLAY MESSAGE: Display Message In The Web Page.
        else:
            form = forms.AddIncomeExpense() # FORM: Instance Of The 'AddIncomeExpense' Form Stored In A Variable. This Will Be Passed Into The 'addPage' Template.

        # CODE PURPOSE: Statements Below Will Acquire The 5 Latest Income/Expense By Date The User Has Submitted So They Can Be Displayed On The Web Page.
        items = IncomeExpense.objects.filter(user = response.user).order_by('-date') # OBJECT FILTER: Get All Income/Expenses A User Has Made And Store It Ordered By Date Descending.
        x = []
        y = len(items)
        if y > 5:
            y = 5
        for i in range(y):
            x.append(items[i])

        context = {"form": form, "items": x}
        return render(response, "main/addPage.html", context)
    else:
        return HttpResponseRedirect("/login") # REDIRECT: If The User Isn't Authenticated Redirect Them To The Login Page.

# VIEW PURPOSE: Display All Income/Expenses The User Has Submitted And Order Them By Date. The User Can Delete A Income/Expense On This Page.
def historyPage(response):
    if response.user.is_authenticated:
        items = IncomeExpense.objects.filter(user = response.user).order_by('date')  # OBJECT FILTER: Get All Income/Expenses A User Has Made And Store It Ordered By Date

        myFilter = FilterIncomeExpense(response.GET, queryset=items) # FILTER: Create Filter Instance.
        items = myFilter.qs # FILTER: Filter Items From Query On Template.

        income = 0  # INCOME RUNNING TOTAL: Running Total For Income.
        expense = 0  # EXPENSE RUNNING TOTAL: Running Total For Expenses.

        for item in items: # FOR LOOP: Loop For The Amount Of Objects In The QuerySet.
            if item.typeIE == "INCOME": # IF STATEMENT: For The Current Object In The QuerySet Check If It Is "INCOME".
                income = income + item.value # INCOME RUNNING TOTAL: Increase The Running Total for 'income' If It Is Based Off Object Value.
            else:
                expense = expense + item.value # EXPENSE RUNNING TOTAL: Else Increase The Running Total for 'expense'.

        context = {"items": items, "myFilter": myFilter, "income": income, "expense": expense}
        return render(response, "main/historyPage.html", context)
    else:
        return HttpResponseRedirect("/login")

# VIEW PURPOSE: Delete An Income/Expense Found On The History Page. This View Essentially Gives Functionality To The Delete Button In 'historyPage.html'.
def deleteItem(response, itemID):
    # Try And Except Statement To Extinguish DoesNotExist Error.
    try:
        item = IncomeExpense.objects.get(id = itemID)  # Get IncomeExpense Object Using itemID Passed In From Button Press.
        item.delete()  # Delete The IncomeExpense Object.
        messages.success(response, "You Have Successfully Deleted " + item.description)  # Display A Message In The Web Page. Pass In The Message.
    except IncomeExpense.DoesNotExist:
        raise Http404  # If IncomeExpense Does Not Exist Go To 404 Page (Page Not Found).

    return HttpResponseRedirect("/history")  # Once The Object Has Been Deleted Remain On The Same Page 'history'.

# VIEW PURPOSE: Edit An Income/Expense Found On The History Page. This View Essentially Gives Functionality To The Edit Button In 'historyPage.html'.
def editTransaction(response, itemID):
    # Try And Except Statement To Extinguish DoesNotExist Error.
    try:
        item = IncomeExpense.objects.get(id = itemID)  # Get IncomeExpense Object Using itemID Passed In From Button Press.

        if response.method == "POST":
            form = forms.AddIncomeExpense(response.POST) # FORM: Get Data From The Submitted Form And Store It In A Variable.

            if form.is_valid(): # IS_VALID(): Check If The Form Is Valid. If The Form Has No Errors It Is Valid.
                typeIE = form.cleaned_data["typeIE"]
                description = form.cleaned_data["description"]
                value = form.cleaned_data["value"]
                value = round(value, 2)
                date = form.cleaned_data["date"]

                obj = IncomeExpense(id = itemID, user = response.user, typeIE = typeIE, description = description, value = value, date = date)  # UPDATE OBJECT: Update 'IncomeExpense' Object Using The Form Values.
                obj.save() # SAVE OBJECT: Save Object Into The Database.
                return HttpResponseRedirect("/editTransaction/"+itemID)  # Once The Object Has Been Deleted Remain On The Same Page 'history'.
        else:
            form = forms.AddIncomeExpense() # FORM: Instance Of The 'AddIncomeExpense' Form Stored In A Variable. This Will Be Passed Into The 'editTransaction' Template.
            form.initial["typeIE"] = item.typeIE # INITIAL VALUE: Set Initial Value Of The 'typeIE' Field.
            form.initial["description"] = item.description # INITIAL VALUE: Set Initial Value Of The 'description' Field.
            form.initial["value"] = item.value # INITIAL VALUE: Set Initial Value Of The 'value' Field.
            form.initial["date"] = item.date # INITIAL VALUE: Set Initial Value Of The 'date' Field.
    except IncomeExpense.DoesNotExist:
        raise Http404  # If IncomeExpense Does Not Exist Go To 404 Page (Page Not Found).

    context = {"item": item, "form": form}
    return render(response, "main/editTransaction.html", context)


# VIEW PURPOSE: Render Settings Page.
def settingsPage(response):
    if response.user.is_authenticated:
        return render(response, "main/settingsPage.html")
    else:
        return HttpResponseRedirect("/login")

# VIEW PURPOSE: Render Settings Page.
class ChangePassword(PasswordChangeView):
    template_name = "main/changePasswordPage.html"
    success_url = reverse_lazy('settingPage')

# VIEW PURPOSE: Render Settings Edit Profile Page Where User Can Change Their Details.
def editProfile(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = forms.EditProfileForm(response.POST, instance=response.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/settings")
        else:
            form = forms.EditProfileForm(instance=response.user)
            context = {"form": form}
            return render(response, "main/editProfilePage.html", context)
    else:
        return HttpResponseRedirect("/login")

# VIEW PURPOSE: Render Settings Delete Page.
def deleteAccount(response):
    if response.user.is_authenticated:
        return render(response, "main/deleteAccount.html")
    else:
        return HttpResponseRedirect("/login")

# VIEW PURPOSE: Delete User If Button is Pressed And Redirect User To Logout Page.
def deleteUser(response, userID):
    try:
        u = User.objects.get(id=userID)
        u.delete()
        return HttpResponseRedirect("/logout")  # Once The Object Has Been Deleted Remain On The Same Page 'history'.

    except User.DoesNotExist:
        messages.error(response, "User does not exist")
        return render(response, 'main/settingsPage.html')

def sendEmail(response):
    if response.method == "POST":
        message = response.POST["message"]
        send_mail("Contact Form", message, settings.EMAIL_HOST_USER, ["kamalabdulhafiz@gmail.com"], fail_silently=False)
    return render(response, 'main/contactPage.html')
