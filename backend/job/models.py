import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User 


class JobType(models.TextChoices):
    Permanent = "Permanent"
    Temporary = "Temporary"
    Intership = "Intership"

class Education(models.TextChoices):
    Bachelors = "Bachelors"
    Masters = "Masters"
    Phd = "Phd"
    
class Industry(models.TextChoices):
    Business = "Business"
    Tech = "Tech"
    Transportation = "Transportation"
    
class Experience(models.TextChoices):
    NO_EXPERIENCE = "NoEXPERIENCE"
    ONE_YEAR = "1 Years"
    TWO_YEAR = "2 Years"
    THREE_PLUS = "3 Years Above"
    

def return_date_time():
    now = datetime.now()
    return now + datetime.timedelta(days=10)


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType = models.CharField(max_length=10, choices=JobType.choices, default=JobType.Permanent)
    education = models.CharField(max_length=10, choices=Education.choices, default=Education.Bachelors)
    industry = models.CharField(max_length=10, choices=Industry.choices, default=Industry.Business)
    experience = models.CharField(max_length=10, choices=Experience.choices, default=Experience.NO_EXPERIENCE)
    salary = models.IntegerField(default=1, validators=[(MinValueValidator(1), MaxValueValidator(10000000))])
    position = models.IntegerField(default=-1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now=True)
    
    
    
    
    