import jwt
from fastapi.security.utils import get_authorization_scheme_param

def create_access_token(data: dict):
    # Implement your access token creation logic here
    # Return the access token
    return jwt.encode(data, "secret_key", algorithm="HS256")

def get_authorization_scheme_param(token: str):
    scheme, param = get_authorization_scheme_param(token)
    return param