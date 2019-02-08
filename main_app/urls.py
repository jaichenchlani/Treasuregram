from django.urls import path, include
from . import views
from config import logger

urlpatterns = [
    path('',views.index)
]
logger.debug("URLPatterns:{0}".format(urlpatterns))