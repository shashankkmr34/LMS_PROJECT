from django import forms
from .models import Sales
from .models import Leads

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = "__all__"

class LeadsForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = "__all__"