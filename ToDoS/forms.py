from django import forms
from .models import Pending

class PendingForm(forms.ModelForm):
    class Meta:
        model = Pending
        fields = ['title', 'user', 'is_resolved']
