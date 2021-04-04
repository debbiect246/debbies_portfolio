from django.db import models

#create database table for the projects class
#each item in the class is a row in the Projects table
#used migrate then makemigrations in the terminal to add to django project
#installed pillow as working with images in the table

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title