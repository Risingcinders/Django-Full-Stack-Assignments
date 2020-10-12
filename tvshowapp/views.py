from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show
import datetime


def listshows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "shows.html", context)


def newshow(request):
    return render(request, "shownew.html")


def newshowprocess(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/TVShowLibrary/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                        release_date=request.POST['date'], desc=request.POST['desc'])
        newestshow = Show.objects.get(title = request.POST['title'])
    return redirect('../shows/' + str(newestshow.id))


def showdetail(request, showid):
    context = {
        "thisshow": Show.objects.get(id=showid)
    }
    return render(request, "showdetail.html", context)


def showedit(request, showid):
    date = Show.objects.get(id=showid).release_date
    date = datetime.date.strftime(date, "%Y-%m-%d")
    context = {
        "thisshow": Show.objects.get(id=showid),
        "datesample": date
    }
    return render(request, "showedit.html", context)


def showeditprocess(request, showid):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/TVShowLibrary/shows/' + str(showid) + '/edit')
    else:
        thisshow = Show.objects.get(id=showid)
        thisshow.title = request.POST['title']
        thisshow.network = request.POST['network']
        thisshow.release_date = request.POST['date']
        thisshow.desc = request.POST['desc']
        thisshow.save()
    return redirect('../' + str(showid))


def showdelete(request, showid):
    thisshow = Show.objects.get(id=showid)
    thisshow.delete()
    return redirect('/TVShowLibrary/shows')


def backtohome(request):
    return redirect('./shows')
