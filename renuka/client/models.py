from django.db import models

# Create your models here.

class BookUser(models.Model):
    name = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=100, blank=False)
    dress_type = models.CharField(max_length=20, blank=False) #dress type
    #measurements
    shoulder_to_shoulder = models.CharField(max_length=20, blank=False)
    above_bust = models.CharField(max_length=20, blank=False)
    top_bust = models.CharField(max_length=20, blank=False)
    below_bust = models.CharField(max_length=20, blank=False)
    blouse_length = models.CharField(max_length=20, blank=False)
    arm_hole = models.CharField(max_length=20, blank=False)
    arm_width = models.CharField(max_length=20, blank=False)
    arm_length = models.CharField(max_length=20, blank=False)
    waist = models.CharField(max_length=20, blank=False)
    saree_length = models.CharField(max_length=20, blank=False)
    saree_waist = models.CharField(max_length=20, blank=False)
    knee_to_knee = models.CharField(max_length=20, blank=False)
    thavani = models.CharField(max_length=20, blank=False)
    pyjama_waist = models.CharField(max_length=20, blank=False)
    pyjama_hip = models.CharField(max_length=20, blank=False)
    pyjama_length = models.CharField(max_length=20, blank=False)
    pyjama_ankle = models.CharField(max_length=20, blank=False)

