from django import forms

from .models import Choice


class VoteForm(forms.Form):
    choice = forms.ChoiceField(choices=Choice.objects.values_list('id', 'choice_text'))
