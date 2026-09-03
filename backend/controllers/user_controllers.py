from services.registerService import register_service
from services.loginService import login_service
def register_user():
    return register_service()

def login_user():
    return login_service()