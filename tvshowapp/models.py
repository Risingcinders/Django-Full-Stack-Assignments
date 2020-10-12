from django.db import models
import datetime


class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['title']) < 2:
            errors["title"] = "Title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network must be at least 3 characters"
        if (len(postData['desc']) < 10) and (len(postData['desc']) != 0):
            errors['desc'] = "Description must be at least 10 characters or left blank"
        if (datetime.date.today() < datetime.datetime.strptime(postData['date'],"%Y-%m-%d").date()):
            errors['date'] = "Date must be in the past"
        shows = Show.objects.all()
        titlelist = []
        for show in shows:
            titlelist.append(show.title)
        # if (Show.objects.get(title = postData['title']) != None):
        if postData['title'] in titlelist:
            errors['duplicate'] = "That show already exists"
        return errors
        
        #title 2 char,
        # network 3 car
        # desc 10 car


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
