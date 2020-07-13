import jwt
from django.conf import settings as conf_settings

from users.models import UserToken

SECRET_KEY = conf_settings.SECRET_KEY


def check_valid_token_format():
    pass


def check_token_validity(request, token):
    try:
        # when jwt iat expires token validation will fail
        payload = jwt.decode(token, SECRET_KEY, verify=False, algorithm='HS256')
        user_id = payload['info']
        request.session['user_id'] = user_id
        count_user_id = UserToken.objects.filter(user_id=user_id).count()
        if int(count_user_id) > 1:
            return False
        else:
            return True
        return False
    except:
        return False


def check_refresh_token_validity(request, token):
    try:
        # when jwt iat expires token validation will fail
        payload = jwt.decode(token, SECRET_KEY)
        print("Payload", payload)
        username = payload['info']
        request.session['username'] = username
        return True
    except:
        return False
