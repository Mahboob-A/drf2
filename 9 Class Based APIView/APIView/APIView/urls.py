

'''
9. Class Based APIViwe in DRF 
300823, Wednesday, 07.00 am 
'''


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
