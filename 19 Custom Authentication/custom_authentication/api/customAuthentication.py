

from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication): 
        '''
        A class for Custom Authentication. 
        Need to override the - authenticate(self, request) method. 
        '''
        def authenticate(self, request):
                # we can add any authentication logic here 
                # username = request.query_params('username')
                username = request.GET.get('username')
                if username is None:
                        
                        # returning None means authentication failed.  
                        return None 
        
                try: 
                        user = User.objects.get(username=username)
                except User.DoesNotExist: 
                        raise AuthenticationFailed('User does not found')
                
                # If no exception is raised, then authenticate the user. 
                return  (user, None)