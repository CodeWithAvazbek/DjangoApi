from django.urls import path, include
from rest_framework import routers
from .views import CourseView

routers = routers.DefaultRouter()
routers.register('courses', CourseView)

urlpatterns = [
    path('', include(routers.urls))
]
