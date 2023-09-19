from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    # for activating signal for auto generating token for newly created user. 
    def ready(self): 
        import api.signals 
