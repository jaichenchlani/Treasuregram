from django.shortcuts import render
from django.http import HttpResponse
from config import logger

# Create your views here.
def index(request):
    logger.debug("Start..")
    logger.debug("Request:{0}".format(request))
    return HttpResponse('<h1>Hello Explorers!<h1>')
