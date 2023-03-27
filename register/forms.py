# Both Statements Below Are Used For User Registration, Sign Up And Login.
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


# DJANGO REGISTRATION: Django Can Do Registration For Us By Using Its Built In 'UserCreationForm'.
# USERCREATIONFORM: Allows Us To Create A User With No Privileges.
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "<span style='font-family: abc, sans-serif'>Email</span>") # FIELD: Here We Are Specifying An EmailField() We Want To Be Included In Our UserCreationForm.

    # FONT: Adding Font To Fields.
    username = forms.CharField(label = "<span style='font-family: abc, sans-serif'>Username</span>")
    first_name = forms.CharField(label = "<span style='font-family: abc, sans-serif'>First Name</span>")
    last_name = forms.CharField(label = "<span style='font-family: abc, sans-serif'>Last Name</span>")
    password1 = forms.CharField(
        label="<span style='font-family: abc, sans-serif'>Password</span>",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="<span style='font-family: abc, sans-serif'>Password Confirmation</span>",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    # META CLASS: Used To Change The Behaviour Of Our Model Fields.
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"] # FIELDS: Here We Are Including The 'email' Field Into The UserCreationForm And Other Django Provided Fields We Want Displayed.

    # PLACEHOLDER: Here We Have Included Placeholder Values To Our Form Fields.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', "style": "border-color: #303030; border-width:3px;"})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', "style": "border-color: #303030; border-width:3px;"})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', "style": "border-color: #303030; border-width:3px;"})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', "style": "border-color: #303030; border-width:3px;"})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', "style": "border-color: #303030; border-width:3px;"})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', "style": "border-color: #303030; border-width:3px;"})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat Password', "style": "border-color: #303030; border-width:3px;"})

# DJANGO AUTHENTICATION: Django Can Do Registration For Us By Using Its Built In 'AuthenticationForm'.
# AUTHENTICATIONFORM: Allows Us To Create A User With No Privileges.
class LoginForm(AuthenticationForm):
    # FONT: Adding Font To Fields.
    username = UsernameField(
        label="<span style='font-family: abc, sans-serif'>Username</span>",
        widget=forms.TextInput(attrs={"autofocus": True})
    )
    password = forms.CharField(
        label="<span style='font-family: abc, sans-serif'>Password</span>",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    # META CLASS: Used To Change The Behaviour Of Your Model Fields.
    class Meta:
        model = User
        fields = ['username', 'password'] # FIELDS: Here We Are Including The Fields We Want In Our Form.

    # PLACEHOLDER: Here We Have Included Placeholder Values To Our Form Fields.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', "style": "border-color: #303030; border-width:3px;"})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', "style": "border-color: #303030; border-width:3px;"})

        # Below Is An Alternative Way Of Doing The Above.
        # self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        # self.fields['username'].label = False
        # self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        # self.fields['password'].label = False
