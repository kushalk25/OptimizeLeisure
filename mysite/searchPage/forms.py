from django import forms

class ActivityForm(forms.Form):
    activity_name = forms.CharField(label='activity', max_length=500)
    activity_duration = forms.IntegerField(label='duration')
