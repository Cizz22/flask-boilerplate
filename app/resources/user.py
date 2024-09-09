from functools import partial

from digital_twin_migration.database import Propagation, Transactional
from digital_twin_migration.models.efficiency_app import User
from flask import Response
from flask_restful import Resource, Response
from flask_restful.reqparse import Argument

from app.repositories import UserRepository
from app.schemas import UserSchema
from core.security import token_required
from core.utils import parse_params, response

user_repository = UserRepository()
user_schema = UserSchema()


class UsersResource(Resource):
    @token_required
    def get(self, user_id: str) -> Response:
        users = user_repository.get_all()
        return response(
            200,
            True,
            "Cases retrieved successfully",
            user_schema.dump(users, many=True),
        )

    @token_required
    @parse_params(Argument("name", location="json", required=True))
    def post(self, name: str, user_id: str) -> Response:
        is_user = user_repository.get_by_name(name)

        if is_user:
            return response(409, False, "User already exists")

        user = user_repository.create({"name": name})
        return response(201, True, "Case created successfully", user_repository.dump(user))


class UserResource(Resource):
    @token_required
    def get(self, usr_id: str, user_id: str) -> Response:
        user = user_repository.get_by_uuid(usr_id)

        if not user:
            return response(404, False, "User not found")

        return response(
            200, True, "Case retrieved successfully", user_repository.dump(user)
        )

    @token_required
    @Transactional(propagation=Propagation.REQUIRED)
    def delete(self, usr_id, user_id) -> Response:
        user = user_repository.get_by_uuid(usr_id)

        if not user:
            return response(404, False, "Case not found")

        user_repository.delete(user)

        return response(200, True, "Case deleted successfully")

    @token_required
    @Transactional(propagation=Propagation.REQUIRED)
    @parse_params(Argument("name", location="json", required=False, default=None))
    def put(self, usr_id, user_id, **attributes) -> Response:
        user = user_repository.get_by_uuid(usr_id)

        if not user:
            return response(404, False, "Case not found")

        user_repository.update(user, attributes)

        return response(200, True, "Case updated successfully")
