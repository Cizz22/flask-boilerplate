"""
Defines the blueprint for the cases
"""

from flask import Blueprint
from flask_restful import Api

from app.resources import UserResource, UsersResource

USERS_BLUEPRINT = Blueprint("users", __name__)

Api(USERS_BLUEPRINT).add_resource(UsersResource, "/users")
Api(USERS_BLUEPRINT).add_resource(UserResource, "/users/<usr_id>")
