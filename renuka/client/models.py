from django.db import models

# Create your models here.

class client(models.Model):
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

class pattern_display(models.Model):
    pattern_image=models.ImageField(upload_to="pattern_images", height_field=None, width_field=None, max_length=None)
    pattern_description=models.CharField(max_length=100, blank=False)   
    pattern_detail=models.CharField(max_length=200, blank=False, default="details here")    

class accessories_display(models.Model):
    accessories_image=models.ImageField(upload_to="accesories_images", height_field=None, width_field=None, max_length=None)
    accessories_description=models.CharField(max_length=100, blank=False)
    accessories_detail=models.CharField(max_length=200, blank=False, default="accessories detailed description here")
    
class ornaments_display(models.Model):
    ornaments_image=models.ImageField(upload_to="ornaments_images", height_field=None, width_field=None, max_length=None)
    ornaments_description=models.CharField(max_length=100, blank=False)
    ornaments_detail=models.CharField(max_length=200, blank=False, default="details here")
