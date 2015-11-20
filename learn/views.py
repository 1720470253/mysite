#-*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from learn.models import *
import datetime
def creat(req):
	Author1 = Author.objects.get(Name="张新")
	Author1.book_set.create(ISBN ="1231231230",Title="操作系统",Publisher="机械",Price="23.00",PublishDate="2015-1-1")
	Author1.book_set.create(ISBN ="1231231231",Title="操作系统1",Publisher="机械汞",Price="23.01",PublishDate="2015-1-2")
	Author1.book_set.create(ISBN ="1231231232",Title="操作系统2",Publisher="机械2",Price="23.02",PublishDate="2015-1-3")
	
	return render_to_response("home.html",{"message":"添加成功"})
def home(req):
	if req.POST:
		host = req.POST
		try:
			author = Author.objects.get(Name = host["name"])
			book = author.book_set.all()
			return render_to_response("home.html",{"books":book})
		except:
			return render_to_response("home.html",{"message":"未找到"})
	return render_to_response('home.html')

def show(req,id):
	if req.POST:
		host = req.POST
		book = Book.objects.get(ISBN = host["del"])
		book.delete()
		return render_to_response("home.html",{"message":"删除成功"})
	book = Book.objects.get(ISBN = id)
	return render_to_response("show.html",{"book":book})