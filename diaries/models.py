from django.db import models

# Create your models here.

class poems(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.TextField(max_length=500,null=True)
    content = models.TextField(max_length=5000,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    poems_image = models.ImageField(null=True,blank=True)
    insta_link = models.URLField(blank=True, null=True)
    fb_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.title

class shayri(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.TextField(max_length=500,null=True)
    content = models.TextField(max_length=5000,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    shayri_image = models.ImageField(null=True,blank=True)
    insta_link = models.URLField(blank=True, null=True)
    fb_link = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ["-date_created"]
    
    def __str__(self):
        return self.title

class oneliners(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.TextField(max_length=500,null=True)
    content = models.TextField(max_length=5000,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    oneliners_image = models.ImageField(null=True,blank=True)
    insta_link = models.URLField(blank=True, null=True)
    fb_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.title
