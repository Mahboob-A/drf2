

'''
11. Concrete View Class in Django REST Framework
050923, Tuesday, 07.00 am 
'''


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
