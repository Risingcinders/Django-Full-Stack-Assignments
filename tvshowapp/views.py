from django.shortcuts import render, HttpResponse, redirect
from .models import Show
import datetime


def listshows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "shows.html", context)


def newshow(request):
    if request.method == 'POST':
        Show.objects.create(
            title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], desc=request.POST['desc'])
    return render(request, "shownew.html")


def newshowprocess(request):
    if request.method == 'POST':
        Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                            release_date=request.POST['date'], desc=request.POST['desc'])
    return redirect('../shows')


def showdetail(request, showid):
    context = {
        "thisshow": Show.objects.get(id=showid)
    }
    return render(request, "showdetail.html", context)


def showedit(request, showid):
    date = Show.objects.get(id=showid).release_date
    date = datetime.date.strftime( date, "%Y-%m-%d")
    context = {
        "thisshow": Show.objects.get(id=showid),
        "datesample" : date
    }
    return render(request, "showedit.html", context)


def showeditprocess(request, showid):
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
