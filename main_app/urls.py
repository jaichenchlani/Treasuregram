from django.urls import path, include
from . import views
from config import logger
from django.views.static import serve

urlpatterns = [
    path('', views.index),
    path('<int:treasure_id>/', views.detail, name='detail'),
    path('post_url/', views.post_treasure, name='post_treasure'),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('like_treasure/', views.like_treasure, name='like')

]
logger.debug("URLPatterns:{0}".format(urlpatterns))

# if settings.DEBUG:
#     urlpatterns += [
#         path('media/', serve, 'document_root': settings.MEDIA_ROOT)
#     ]