from django.shortcuts import render
# подключаем объект для http запросов
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Успешно!")