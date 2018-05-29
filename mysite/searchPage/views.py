from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Activity
from .forms import AddActivityForm, FindActivityForm
import math

def index(request):

    alert = ''

    if request.method == 'POST':
        form = AddActivityForm(request.POST)

        if form.is_valid():
            new_activity = Activity(
                name=form.cleaned_data['activity_name'],
                duration=timeInSeconds(
                    form.cleaned_data['activity_hours'],
                    form.cleaned_data['activity_minutes'],
                ),
            )
            new_activity.save()
            alert = 'success'
        else:
            alert = 'failure'

    addForm = AddActivityForm(initial={
        'activity_hours': 0,
        'activity_minutes': 0,
    })

    findForm = FindActivityForm(initial={
        'activity_hours': 0,
        'activity_minutes': 0,
    })

    return render(request, "searchPage/home.html", {
        'alert': alert,
        'addForm': addForm,
        'findForm': findForm,
    })


def results(request):
    if request.method == 'POST':
        form = FindActivityForm(request.POST)

        if form.is_valid():
            activities = Activity.objects.filter(duration__lte=timeInSeconds(
                form.cleaned_data['activity_hours'],
                form.cleaned_data['activity_minutes'],
            ))
        else:
            # show errors
            activities = Activity.objects.all()

    else:
        activities = Activity.objects.all()

    processed = []

    for activity in activities:
        hours, mins = formattedTime(activity.duration)
        processed.append({
            'id': activity.id,
            'name': activity.name,
            'hours': hours,
            'minutes': mins,
        })

    return render(request, "searchPage/results.html", {'activities': processed})


def delete(request, id):
    activity = get_object_or_404(Activity, pk=id) # note: pk means primary key
    activity.delete()
    return HttpResponse('')


def formattedTime(seconds):
    # remove seconds
    seconds -= seconds % 60

    # calc mins and hours
    mins = seconds / 60
    hours = mins / 60

    return math.floor(hours), math.floor(mins % 60)


def timeInSeconds(hours, minutes):
    return hours*3600 + minutes * 60
