

'''
16. Custom Permission in DRF 

Subclass from BasePermission and override the has_permission(self, request, view) for general view wise permission 
or override has_object_permission(self, request, view, obj) for object level permission 

'''

from rest_framework.permissions import BasePermission

# Thsese are just basic examples of custom permissons 
class IsOnlyGET(BasePermission): 
        '''
        A custom permission class for allowing only GTE requests. 
        '''
        def has_permission(self, request, view):
                if request.method == 'GET': 
                        return True 
                return False 
        
class IsOnlyPOST(BasePermission): 
        '''
        A custom permission class for allowing only POST requests. 
        '''
        def has_permission(self, request, view):
                if request.method == 'POST': 
                        return True 
                return False 