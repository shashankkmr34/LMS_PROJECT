from django import forms
from .models import sales
from .models import leads

class salesform(forms.ModelForm):
    class Meta:
        model = sales
        fields = "__all__"

class leadsform(forms.ModelForm):
    class Meta:
        model = leads
        fields = "__all__"