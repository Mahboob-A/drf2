
# A class for custom auth token 

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken): 
        '''
        A custom class to return additional information of the user along with the auth token. 
        '''
        def post(self, request, *args, **kwargs): 
                serializer = self.serializer_class(data=request.data, context={'request' : request})
                serializer.is_valid(raise_exception=True)
                user = serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                # print("token: " , token)
                # print("created: ", created)
                return Response({
                        'token' : token.key, 
                        'user_id' : user.pk, 
                        'email' : user.email, 
                        'username' : user.username, 
                })
