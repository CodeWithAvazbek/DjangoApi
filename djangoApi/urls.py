
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Courses Api Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls'))
]
