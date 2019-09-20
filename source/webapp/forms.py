from django import  forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES

class TaskForm(forms.Form):

    description = forms.CharField(max_length=200, required=True, label='Description')

    status = forms.ChoiceField(required=True, label='Status', choices=STATUS_CHOICES)

    date_perf = forms.CharField(required=False, max_length=50, label='Finish Date')

    detail = forms.CharField(required=False, max_length=400, label='Details')

