from django.shortcuts import render
# from django.http import HttpResponse
from config import logger
from .models import Treasure

# Create your views here.
def index(request):
    # logger.debug("Start..")
    # logger.debug("Request:{0}".format(request))
    treasures = Treasure.objects.all()
    logger.debug(str(render(request,'index.html',{"treasures": treasures})))
    return render(request,'index.html', {"treasures": treasures})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    logger.debug(treasure)
    return render(request,'detail.html', {"treasure": treasure})


# class Treasure:
#     def __init__(self, name, value, material, location, img_url):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#         self.img_url = img_url
    
# treasures = [
#     Treasure("Gold Nugget", 500.00, "gold", "Curly's Creek, NM","static/images/gold-nugget.jpeg"),
#     Treasure("Fool's Gold", 0, "pyrite", "Fool's Falls, CO","static/images/fools-gold.jpeg"),
#     Treasure("Coffee Can", 20.00, "tin", "Acme, CA","static/images/coffee-can.jpeg")
# ]
# logger.debug(treasures)