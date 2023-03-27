from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Create your models here.

# DEFINING MODELS: Allows You To Create And Store Objects In A Database.
# CHANGES MADE TO MODELS.PY: python manage.py makemigrations 'app name', python manage.py migrate. (Type In Terminal).
# ANY NEW DEPENDENCIES: python manage.py makemigrations, python manage.py migrate. (Type In Terminal).

# HOW TO CREATE AND SAVE OBJECTS. (TYPE IN TERMINAL). -
# python manage.py shell
# from 'app name'.models import model1, model2 ...
# x = model1(y="...")
# x.save()

# HOW TO VIEW ALL OR ONE OBJECT(S) STORED IN THE DATABASE FOR A MODEL. (TYPE IN TERMINAL). -
# model1.objects.all() (QuerySet Will Be Shown)
# model1.objects.get(id=1)
# model1.objects.get(y="...")

# VIEW ITEMS IN A SET. (TYPE IN TERMINAL). -
# x.item_set.all() (EMPTY QUERY SET)

# CREATE AND GET ITEMS FOUND IN A SET. (TYPE IN TERMINAL). -
# x.item_set.create(text="...", complete=False)
# x.item_set.all()
# x.item_set.get(id=1)
# x.item_set.get(y="...")

# CHOICES DICTIONARY: Below Is A Dictionary For The Choices Displayed In 'typeIE'.
INCOME_EXPENSE_CHOICES = (
    ("INCOME", "Income"),
    ("EXPENSE", "Expense"),
)

class IncomeExpense(models.Model):
    # USER: Assign The Current User To The Income/Expense Object.
    # TYPEIE: CharField Variable. Is The User Inputting An Income Or Expense.
    # DESCRIPTION: CharField Variable. Information About The Income/Expense.
    # VALUE: FloatField Variable. Value Of The Income/Expense.
    # DATE: DateField Variable. Date Of The Income/Expense. Widget Allows For The Date Picker.
    user = models.ForeignKey(User, on_delete = CASCADE, related_name = "user", null = True)
    typeIE = models.CharField(max_length = 10, choices = INCOME_EXPENSE_CHOICES)
    description = models.CharField(max_length = 20)
    value = models.FloatField()
    date = models.DateField()

    # DEF __STR__(SELF): Alter Output So That It Is More Pleasing For When An Object Is Printed Or Displayed On The Admin Site.
    def __str__(self):
        return self.description
