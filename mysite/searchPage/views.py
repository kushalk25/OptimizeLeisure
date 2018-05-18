from django.shortcuts import render
from .models import Activity
from .forms import ActivityForm

def index(request):
    form = ActivityForm()
    return render(request, "searchPage/home.html", {'form': form})


def results(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)

        if form.is_valid():
            new_activity = Activity(
                name=form.cleaned_data['activity_name'],
                duration=form.cleaned_data['activity_duration'],
            )
            new_activity.save()
        else:
            # show errors

    activities = Activity.objects.all()
    return render(request, "searchPage/results.html", {'activities': activities})
