from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    id = models.AutoField
    user_id = models.CharField(max_length=20, primary_key=True)
    real_name = models.CharField(max_length=20)
    tz = models.CharField(max_length=30)

    def __str__(self):
        return self.real_name



class ActivityPeriod(models.Model):
    id = models.AutoField
    user_id = models.CharField(max_length=20)
    start_time = models.CharField(max_length=40)
    end_time = models.CharField(max_length=40)

    def __str__(self):
        return self.id1