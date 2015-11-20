#-*-coding: utf-8-*-
#!/usr/bin/python

from django.db import models
 
class Author(models.Model):
    AuthorID  =  models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 30)
    Country = models.CharField(max_length = 30)
    Age = models.IntegerField()
	
class Book(models.Model):
	Title = models.CharField(max_length = 30)
	AuthorID = models.ForeignKey(Author,null=True)
	Publisher = models.CharField(max_length = 30)
	PublishDate = models.DateField()
	ISBN = models.CharField(max_length = 30)
	Price = models.FloatField()
 