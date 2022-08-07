import logging
import functools
from models.user import UserModel
from hmac import compare_digest
from flask import request


logger = logging.getLogger(__name__)


def is_valid(api_key):
    user = UserModel.find_by_key(api_key)
    if user and compare_digest(user.user_key, api_key):
        return True


def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if request.args:
            api_key = request.args.get('api_key', default=None, type=str)
        else:
            logger.error("User did not provide an API key")
            return {"message": "Please provide an API key"}, 400
        # Check if API key is correct and valid
        if is_valid(api_key):
            return func(*args, **kwargs)
        else:
            logger.error("The provided API key is not valid")
            return {"message": "The provided API key is not valid"}, 403
    return decorator
