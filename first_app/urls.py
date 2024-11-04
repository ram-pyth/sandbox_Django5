from django.urls import path, include
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

urlpatterns = [
    path('', views.courses, name='courses'),
    path('modules/', views.modules, name='modules')
]
