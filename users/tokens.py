from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


user = get_user_model()

def create_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }   
