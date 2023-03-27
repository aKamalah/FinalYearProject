from django.urls import path
from main import views

# URL PATH: Navigate To A View Which Will Provide A HTML Page Through A Specified URL Path.
# <> (CAPTURE): Value Within Capture Will Be Passed Into A View Parameter.
# <>: 'itemID' Is Used To Find Out Which Income/Expense To Delete. It Is Passed Into 'deleteItem'.
# <>: 'itemID' Is Used To Find Out Which Income/Expense To Edit. It Is Passed Into 'editTransaction'.
# <>: 'userID' Is Used To Find Out Which User To Delete. It Is Passed Into 'deleteUser'.
urlpatterns = [
    path("", views.welcomePage, name = "welcomePage"),
    path("home/", views.homePage, name = "homePage"),
    path("add/", views.addPage, name = "addPage"),
    path("history/", views.historyPage, name = "historyPage"),
    path("deleteItem/<itemID>", views.deleteItem, name = "deleteItem"),
    path("editTransaction/<itemID>", views.editTransaction, name = "editTransaction"),
    path("settings/", views.settingsPage, name = "settingPage"),
    path("settings/changePassword", views.ChangePassword.as_view(), name="changePasswordPage"),
    path("settings/editProfile", views.editProfile, name="editProfile"),
    path("settings/deleteAccount", views.deleteAccount, name="deleteAccount"),
    path("deleteUser/<userID>", views.deleteUser, name="deleteUser"),
    path("contact", views.sendEmail, name="contactPage")
]
