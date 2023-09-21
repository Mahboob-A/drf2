

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


'''
This signal is responsible for creating Auth Token for Users whenever a User is created.
Import the signal in a model.py file 
'''

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs): 
        if created: 
                Token.objects.create(user=instance)
                