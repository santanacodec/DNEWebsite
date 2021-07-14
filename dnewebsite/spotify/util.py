from .models import SpotifyToken
from django.utils import timezone
from datetime import timedelta

def get_user_token(session_id):
    user_token = SpotifyToken.objects.filter(user = session_id)
    if user_token.exists():
        return user_token[0]
    else:
        return None
def something(session_id,access_token, token_type,expires_in):
    token = get_user_token(session_id)
    expires_in = timezone.now + timedelta(seconds=7200)
    if token:
        