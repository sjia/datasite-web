from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('all/', views.data_list),
    path('detail/<int:pk>', views.data_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
