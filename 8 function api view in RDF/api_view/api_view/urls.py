

'''
8. Function Based @api_view() in DRF 
290823, Tuesday, 10.00 am 
'''


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple_api/', include('basic_api_view.urls')),
    path('api/', include('crud_api_view.urls')),
]
