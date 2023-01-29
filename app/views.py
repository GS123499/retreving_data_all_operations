from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='Cricket')

    
    d={'topics':QST}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSW=Webpages.objects.all()
    QSW=Webpages.objects.filter(topic_name='Cricket')
    QSW=Webpages.objects.exclude(topic_name='Cricket')
    QSW=Webpages.objects.all().order_by(Length('name'))
    QSW=Webpages.objects.all().order_by(Length('name').desc())
    QSW=Webpages.objects.filter(url__startswith='https')
    QSW=Webpages.objects.filter(url__startswith='D')
    QSW=Webpages.objects.filter(url__endswith='https')
    QSW=Webpages.objects.filter(name__startswith='J')
    QSW=Webpages.objects.filter(name__endswith='h')
    QSW=Webpages.objects.filter(name__contains='a')
    QSW=Webpages.objects.filter(name__in=['Ganesh','Joshna','shiva'])

    QSW=Webpages.objects.filter(Q(topic_name='Cricket') | Q(name='Ganesh'))
    QSW=Webpages.objects.filter(Q(topic_name='Cricket') & Q(url__startswith='https'))
    QSW=Webpages.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_Access(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='2022-1-24')
    QSA=AccessRecords.objects.filter(date__gt='2012-1-24')
    QSA=AccessRecords.objects.filter(date__gte='2001-01-24')
    QSA=AccessRecords.objects.filter(date__lte='10-01-1945')
    QSA=AccessRecords.objects.filter(date__year='1945')
    QSA=AccessRecords.objects.filter(date__month='10')
    QSA=AccessRecords.objects.filter(date__day='10')
    QSA=AccessRecords.objects.filter(date__year__gt='1998')

    QSA=AccessRecords.objects.all()
    d={'Access':QSA}
    return render(request,'display_Access.html',d)

def update_webpages(request):
    Webpages.objects.filter(name='sindhu').update(url=https://sindhu.com)
    76yhWebpages.objects.all()
    return render(request,'display_webpages.html')