from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.addauthor),
    path('', views.addbook),
    path('books/<int:bookid>', views.book),
    path('authors/<int:authorid>', views.author),
    path('books', views.backtohome)
]
