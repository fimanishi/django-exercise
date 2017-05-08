from django.template.response import TemplateResponse

def homepage (request):
    context = {
    "page_title": "HOME PAGE",
    "name": "test",
    "numbers": [1,2,3,4],
    }
    return TemplateResponse(request, 'homepage.html', context)

def animals (request):
    context = {
    "page_title": "Animals",
    "year": 1977,
    }
    return TemplateResponse(request, 'animals.html', context)

def darkside (request):
    context = {
    "page_title": "Dark Side of the Moon",
    "year": 1973,
    }
    return TemplateResponse(request, 'darkside.html', context)

def meddle (request):
    context = {
    "page_title": "Meddle",
    "year": 1971,
    }
    return TemplateResponse(request, 'meddle.html', context)
