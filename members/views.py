from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from members.models import Member
# Create your views here.



def members(request):
    template = loader.get_template('all_members.html')
    context = {
        "mymembers" : Member.objects.all().values(),
    }
    return HttpResponse(template.render(context, request))




