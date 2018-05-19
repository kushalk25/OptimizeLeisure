from django import forms

class AddActivityForm(forms.Form):
    activity_name = forms.CharField(label='activity', max_length=500)
    activity_hours = forms.IntegerField(label='hours')
    activity_minutes = forms.IntegerField(label='minutes')


class FindActivityForm(forms.Form):
    activity_hours = forms.IntegerField(label='hours')
    activity_minutes = forms.IntegerField(label='minutes')
