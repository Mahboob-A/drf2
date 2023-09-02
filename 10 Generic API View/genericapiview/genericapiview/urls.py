

'''
10. GenericAPIView and ModelMixins in DRF 
020923, Saturday, 07.00 am 
'''


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
