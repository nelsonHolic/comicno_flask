from datetime import timedelta

from flask import request
from flask_restx import Namespace, Resource
import jsonref

from .schema_models import Token, UserCreation, UserLogin
from .security import ACCESS_TOKEN_EXPIRE_MINUTES, create_user, fake_users_db, create_access_token, authenticate_user

api = Namespace('user', description='Users related operations')

token_schema = api.schema_model("Token", jsonref.loads(Token.schema_json()))
login_user_schema = api.schema_model("UserLogin", jsonref.loads(UserLogin.schema_json()))
user_creationg_schema = api.schema_model("User", jsonref.loads(UserCreation.schema_json()))


@api.route("/token")
class TokenResource(Resource):
    
    @api.doc('get_jwt_token')
    @api.expect(login_user_schema, validate=True)
    @api.response(201, "this is my response of token", token_schema)
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = authenticate_user(fake_users_db, username, password)
        if not user:
            return "bad request", 401

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}


@api.route("/")
class UserApi(Resource):
    
    @api.doc('create_user')
    @api.expect(user_creationg_schema, validate=True)
    @api.response(201, "this is my response of creation")
    def post(self):
        user = create_user(request.get_json())
        
        return { 'status': "success", 'result':  user}
