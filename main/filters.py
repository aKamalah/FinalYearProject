import django_filters
from django_filters import DateFilter, filters
from .models import IncomeExpense
from django import forms
from django.forms.widgets import TextInput

# DATE PICKER: Here We Are Creating Our Own Input So That We Can Pass It In As A Widget To A DateField Allowing For A Date Picker.
class DateInput(forms.DateInput):
    input_type = "date" # INPUT_TYPE: DateInput By Default Uses Input Type 'text'. The Type Has Been Changed To 'date' So The User Doesn't Manually Type A Date.

# FILTER INCOME EXPENSE: Build Filter System For 'IncomeExpense' Model.
class FilterIncomeExpense(django_filters.FilterSet):
    # FIELDS: Creating Our Own Fields For The Filter Class.
    # DATE1 & DATE2: IncomeExpense Objects From A Specified Range Of Dates.
    # DESCRIPTION: 'icontains' Display Object If  Description Contains A Set Of Characters.
    # VALUE: 'exact' Display Object If Exact Search Value.
    date1 = DateFilter(field_name="date", lookup_expr="gte", widget=DateInput)
    date2 = DateFilter(field_name="date", lookup_expr="lte", widget=DateInput)
    description = filters.CharFilter(field_name="description", lookup_expr="icontains", widget=TextInput(attrs={'placeholder': 'Description'}))
    value = filters.CharFilter(field_name="value", lookup_expr="exact", widget=TextInput(attrs={'placeholder': 'Value'}))

    class Meta:
        model = IncomeExpense
        fields = "__all__" # FIELDS: Include All Fields In 'IncomeExpense' Model.
        exclude = ["user", "date"] # EXCLUDE: Exclude Fields That Should Not Be Displayed.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['typeIE'].label = "Income or Expense" # LABEL: Change Label Name For 'typeIE' So It Is More Pleasing.
