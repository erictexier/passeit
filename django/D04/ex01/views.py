from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404

contents = [
    {   'tag': 'intro',
        'data': 'Django (/ˈdʒæŋɡoʊ/ JANG-goh; stylised as django)[4] is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern.[5][6] It is maintained by the Django Software Foundation (DSF), an independent organization established as a 501(c)(3) non-profit.'
    },
    {   'tag': 'goal',
        'data': "Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and \"pluggability\" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.[7] Python is used throughout, even for settings files and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models."
    },
    {   'tag' : 'history',
        'data': "Django was created in the fall of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. Jacob Kaplan-Moss was hired early in Django’s development shortly before Simon Willison's internship ended.[16] It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt.[17] In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future.[18] In July 2015, Revolution Systems, a software consulting company connected to some Django co-founders and developers, hosted 10th anniversary events in Lawrence.[19]"
    }
    ]

affichages = [
    {   'tag': 'intro',
        'data': 'Describe the processus of showing a static page'},
    {   'tag': 'step1',
        'data': "in setting:  add 'django.contrib.staticfiles' to list ~~INSTALLED_APPS~~"},
    {   'tag' : '2 stage',
        'data': "step2"}
    ]

template_engined = [
    {   'tag': 'intro',
        'data': 'Describe the django template engine'},
    {   'tag': 'Blocks',
        'data': "How blocks works: {% block content %} ... {% endblock content %}\n and there are extended with {% extends 'ex01/commun.html' %}"},
    {   'tag' : 'For loop',
        'data': "How for loop works: {% for x in array %} ... {% endfor%}"},
    {   'tag' : 'If statement',
        'data': "How if statement are implemented: {% if condition %} ...({% else %}) ... {% endif%}"},
    {   'tag' : 'Variables:',
        'data': "How to display variable passed are arguments to template:\n {{variable}}"}
    ]

# Create your views here.
def index(request):
    context = { 'contents': contents, 
                'title': 'Ex01 : Django, framework web.'}
    return render(request, 'ex01/django_history.html', context)

def affichage(request):
    context = { 'contents': affichages, 
                'title': 'Ex01 : Processus d’affichage d’une page statique'}
    return render(request, 'ex01/affichage.html', context)

def template_engine(request):
    context = { 'contents': template_engined, 
                'title': 'Ex01 : Moteur de template.',
                'styling': "FOO"}
    return render(request, 'ex01/template_engined.html', context)
