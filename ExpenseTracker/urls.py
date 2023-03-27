from django.contrib import admin
from django.urls import path, include
import register.views
from django.contrib.auth import views as auth_views
from register.forms import LoginForm

# URL PATH: Navigate To A View Which Will Provide A HTML Page Through A Specified URL Path.
# INCLUDE() METHOD: Access URL Paths Found In Another Applications .urls File.

urlpatterns = [
    path("admin/", admin.site.urls), # ADMIN: URL Path To The Provided Django Admin Site.
    path("", include("main.urls")), # MAIN: Allows Access To The URL Paths Found In 'main.urls'.
    path("register/", register.views.registerPage, name = "register"), # REGISTER: Path To The Register Page View Found In The Application 'register'.
    path("login/", auth_views.LoginView.as_view(template_name = "registration/login.html", authentication_form = LoginForm), name = "login"), # LOGIN: Login Form Path.
    path("logout/", register.views.logoutPage), # LOGIN: Path To The Logout Page View Found In The Application 'register'.
    # RESET PASSWORD: Submit Email Form.
    # RESET EMAIL SENT: Email Sent Message Page.
    # RESET FORM: Link To Password Reset Form Found In Email.
    # RESET PASSWORD COMPLETE: Password Successfully Changed Message.
    # NAME: Must Specify Name As Each View Depend On Each Other.
    path("resetPassword/", auth_views.PasswordResetView.as_view(template_name = "registration/resetPassword.html"), name = "reset_password"),
    path("resetPasswordSent/", auth_views.PasswordResetDoneView.as_view(template_name = "registration/resetPasswordSent.html"), name = "password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name = "registration/resetPasswordConfirm.html"), name = "password_reset_confirm"),
    path("resetPasswordComplete/", auth_views.PasswordResetCompleteView.as_view(template_name = "registration/resetPasswordComplete.html"), name = "password_reset_complete")
]

# The Comment Below Is An Alternative For The Login And Logout Path.
# path("", include("django.contrib.auth.urls")),
# LOGIN & LOGOUT: Access URL Paths Found In 'django.contrib.auth.urls' Provided By Django Particularly 'login/' And 'logout/'.
# We Don't Need To Code The Logout Functionality But No Web Page Will Be Provided Which Isn't Ideal For Me.
# No Placeholder Values Will Be Shown On The Form And The Customisation For The Login Form Will Be Limited.
