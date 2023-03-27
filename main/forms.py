from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

# DJANGO FORMS: Django Can Generate Forms. Saving Time Coding And Providing Already Built-In Features.
# FORM CLASS: Below Are Form Classes With Fields With Their Respective Data Types We Want To Be Displayed.
# LABELS: If There Is No Label In A Field Django Will Display The Variable Name As The Label.

# CHOICES DICTIONARY: Below Is A Dictionary For The Choices Displayed In 'typeIE'.
INCOME_EXPENSE_CHOICES = (
    ("", "----------"), # PLACEHOLDER: "" Placeholder Value For ChoiceField Variable Else Income Will Be Displayed First. This Value Cannot Be Submitted.
    ("INCOME", "Income"),
    ("EXPENSE", "Expense"),
)

# DATE PICKER: Here We Are Creating Our Own Input So That We Can Pass It In As A Widget To A DateField Allowing For A Date Picker.
class DateInput(forms.DateInput):
    input_type = "date" # INPUT_TYPE: DateInput By Default Uses Input Type 'text'. The Type Has Been Changed To 'date' So The User Doesn't Manually Type A Date.

class AddIncomeExpense(forms.Form):
    class Meta:
        model = User
    # TYPEIE: ChoiceField Variable. Is The User Inputting An Income Or Expense.
    # DESCRIPTION: CharField Variable. Information About The Income/Expense.
    # VALUE: FloatField Variable. Value Of The Income/Expense.
    # DATE: DateField Variable. Date Of The Income/Expense. Widget Allows For The Date Picker.
    typeIE = forms.ChoiceField(choices = INCOME_EXPENSE_CHOICES, label = "<span style='font-family: abc, sans-serif'>Income Or Expense</span>")
    description = forms.CharField(max_length = 20, label = "<span style='font-family: abc, sans-serif'>Description</span>")
    value = forms.FloatField(label = "<span style='font-family: abc, sans-serif'>Value (£)</span>")
    date = forms.DateField(widget = DateInput, label = "<span style='font-family: abc, sans-serif'>Date</span>")

    # PLACEHOLDER: Here We Have Included Placeholder Values To Our Form Fields And Provided CSS Styling.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["typeIE"].widget.attrs.update({"style": "border-color: #FAB162; border-width:3px; font-family: abc, serif-san;"})
        self.fields["description"].widget.attrs.update({"placeholder": "Description", "style": "border-color: #FAB162; border-width:3px; font-family: abc, serif-san;"})
        self.fields["value"].widget.attrs.update({"placeholder": "Value (£)", "style": "border-color: #FAB162; border-width:3px; font-family: abc, serif-san;"})
        self.fields["date"].widget.attrs.update({"style": "border-color: #FAB162; border-width:3px; font-family: abc, serif-san;"})

class EditProfileForm(UserChangeForm):
    # EMAIL: EmailField Variable. Users Email.
    # FIRST_NAME: CharField Variable. Users First Name.
    # LAST_NAME: CharField Variable. Users Last Name.
    email = forms.EmailField(label="<span style='font-family: abc, sans-serif'>Email</span>")
    first_name = forms.CharField(label = "<span style='font-family: abc, sans-serif'>First Name</span>")
    last_name = forms.CharField(label = "<span style='font-family: abc, sans-serif'>Last Name</span>")

    # META CLASS: Used To Change The Behaviour Of Your Model Fields.
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name") # FIELDS: Specifying Fields To Be Shown In The Form.

    # PLACEHOLDER: Here We Have Included Placeholder Values To Our Form Fields And Provided CSS Styling.
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields["email"].widget.attrs.update({"style": "border-color: #FAB162; border-width:3px; font-family: abc, serif-san;"})
        self.fields["first_name"].widget.attrs.update({"style": "border-color: #FAB162; border-width:3px; font-family: abc, serif-san;"})
        self.fields["last_name"].widget.attrs.update({"style": "border-color: #FAB162; border-width:3px; font-family: abc, serif-san;"})
        self.fields['password'].widget = forms.HiddenInput()

