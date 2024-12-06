from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


def is_user_authenticated(token):
    """
    Проверяет, авторизован ли пользователь по переданному JWT-токену.

    :param token: Строка токена (Bearer <token>)
    :return: True, если токен валиден, иначе False
    """
    jwt_auth = JWTAuthentication()
    try:
        # Попытка проверить токен
        validated_token = jwt_auth.get_validated_token(token)
        # Если токен валиден, вернем True
        user = jwt_auth.get_user(validated_token)
        return True
    except AuthenticationFailed:
        # Если токен недействителен или истек
        return False
