from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.listshows),
    path('shows/new', views.newshow),
    path('shows/create', views.newshowprocess),
    path('shows/<int:showid>', views.showdetail),
    path('shows/<int:showid>/edit', views.showedit),
    path('shows/<int:showid>/update', views.showeditprocess),
    path('shows/<int:showid>/destroy', views.showdelete),
    path('', views.backtohome)
]
