from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Court

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def courts(request):
  mycourts = Court.objects.all().values()
  template = loader.get_template('all_courts.html')
  context = {
    'mycourts': mycourts,
  }
  return HttpResponse(template.render(context, request))

def details_courts(request, id):
  mycourt = Court.objects.get(id=id)
  template = loader.get_template('details_courts.html')
  context = {
    'mycourt': mycourt,
  }
  return HttpResponse(template.render(context, request))
'''
#
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

#
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")
'''