import logging

from flask_restful import Resource, reqparse
from models.user import UserModel


logger = logging.getLogger(__name__)


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            logger.error("A user with that username already exists")
            return {"message": "A user with that username already exists"}, 400

        logger.info("Creating user")
        user = UserModel(data['username'])
        user.save_to_db()
        logger.info("User created successfully.")

        return {"message": "User created successfully.", "api_key": user.user_key}, 201
