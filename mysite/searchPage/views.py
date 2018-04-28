from django.shortcuts import render

def index(request):
    return render(request, "searchPage/home.html")


def results(request):
    return render(request, "searchPage/results.html")
