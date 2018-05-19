from django.shortcuts import render
from .models import Activity
from .forms import ActivityForm
import math

def index(request):
    form = ActivityForm(initial={
        'activity_hours': 0,
        'activity_minutes': 0,
    })
    return render(request, "searchPage/home.html", {'form': form})


def results(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)

        if form.is_valid():
            new_activity = Activity(
                name=form.cleaned_data['activity_name'],
                duration=timeInSeconds(
                    form.cleaned_data['activity_hours'],
                    form.cleaned_data['activity_minutes'],
                ),
            )
            new_activity.save()
        else:
            # show errors
            pass

    activities = Activity.objects.all()
    processed = []

    for activity in activities:
        hours, mins = formattedTime(activity.duration)
        processed.append({
            'name': activity.name,
            'hours': hours,
            'minutes': mins,
        })

    return render(request, "searchPage/results.html", {'activities': processed})


def formattedTime(seconds):
    # remove seconds
    seconds -= seconds % 60

    # calc mins and hours
    mins = seconds / 60
    hours = mins / 60

    return math.floor(hours), math.floor(mins % 60)


def timeInSeconds(hours, minutes):
    return hours*3600 + minutes * 60
