from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from members.models import Member
# Create your views here.

def main(request):
    return HttpResponse(loader.get_template('main.html').render())

def members(request):
    template = loader.get_template('all_members.html')
    context = {
        "mymembers" : Member.objects.all().values(),
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('details.html')

    context = {
        'mymember' : Member.objects.get(id=id),
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    context = {
        'fruits' : ['apple', 'banana', 'orange', 'watermelon'],
    }
    return HttpResponse(loader.get_template('testing.html').render(context, request))
    