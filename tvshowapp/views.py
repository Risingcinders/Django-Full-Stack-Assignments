from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
import random


def addauthor(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name=request.POST['first'], last_name=request.POST['last'], notes=request.POST['notes'])
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }
    return render(request, "addauthor.html", context)


def addbook(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'], desc=request.POST['desc'])
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }
    return render(request, "addbook.html", context)


def author(request, authorid):
    thisauthor = Author.objects.get(id=authorid)
    if request.method == 'POST':
        booktoaddtodb = Book.objects.get(id=request.POST['booktoadd'])
        thisauthor.books.add(booktoaddtodb)
    context = {
        "authoredbooks": Author.objects.get(id=authorid).books.all(),
        "author": Author.objects.get(id=authorid),
        "otherbooks": Book.objects.exclude(authors=Author.objects.get(id=authorid))

    }
    return render(request, "author.html", context)


def book(request, bookid):
    thisbook = Book.objects.get(id=bookid)

    if request.method == 'POST':
        authortoaddtodb = Author.objects.get(id=request.POST['authortoadd'])
        thisbook.authors.add(authortoaddtodb)
    context = {
        "booksauthors": Book.objects.get(id=bookid).authors.all(),
        "book": Book.objects.get(id=bookid),
        "otherauthors": Author.objects.exclude(books=Book.objects.get(id=bookid))
    }
    return render(request, "book.html", context)

def backtohome(request):
    return redirect('/booksandauthors')