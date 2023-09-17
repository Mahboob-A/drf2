

'''
17. Authentication and Permission in Function Based View  
170923, Sunday, 09.00 pm 
'''


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('crud_api_view.urls')),
]
