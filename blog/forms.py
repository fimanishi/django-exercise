from django import forms

class ClassForm (forms.Form):
    choice_field = forms.ChoiceField()
