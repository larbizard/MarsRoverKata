from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^move/([0-9]+)$',views.moveRoverApi)
]