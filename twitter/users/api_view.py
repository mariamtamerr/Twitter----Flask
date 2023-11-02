

from flask_restful import Resource, fields, marshal_with , abort ##reosurce bta3 elserialization, fields from rest
from flask import make_response ## to return data
from twitter.models import User, db
from twitter.users.parser import user_parser





# 2) SERIALIZATION OF DATA

post_serializer = {
    # "id": fields.Integer,
    "title": fields.String,
    "content": fields.String,
    "user_id": fields.Integer,

}


user_serializer = {
    "id": fields.Integer,
    "username": fields.String,
    "posts": fields.Nested(post_serializer)
}

# -------------------------------------------
# SERIALIZING , POST , GET 
# ---------------------------------------

class UserList(Resource):
    
    @marshal_with(user_serializer)
    def get(self):
        users = User.query.all() #get all users objects
        return users, 200 
    
    @marshal_with(post_serializer)
    def post(self):
        user_args = user_parser.parse_args() # it will take data gyalak fl post w ytabba2 3aleha
        print(user_args)
        user = User.create_user(user_args)
        print("this is user : " , user )
        return user, 201 
    
    #     {
    #     "username": "lalaaa12",
    #     "password": "1234566789@l",
    #     "email": "lalaaa@gmail.com",
    #     "image": "default.jpg"
       
    # }


# ----------------------------------------------------------------
    # ----------------- CRUD OPERATIONS -------------------
# ----------------------------------------------------------------

class UserResource(Resource):

    @marshal_with(user_serializer)
    def get(self, user_id):
        user = User.get_specific_user(user_id)
        return user, 200


    @marshal_with(user_serializer)
    def put(self, user_id):
        user = User.get_specific_user(user_id)
        if user:
            user_args = user_parser.parse_args()
            user.username=user_args["username"]
            user.password=user_args["password"]
            user.email=user_args["email"]
            user.image=user_args["image"]
            db.session.add(user)
            db.session.commit()
            return user, 200
        abort(404, message="user Object Not Found")
  


    def delete(self,user_id):
         user = User.get_specific_user(user_id)
         if user:
             db.session.delete(user)
             db.session.commit()
             response = make_response("Deleted", 204)
             return response
         abort(404, message="Delete Object Not Found")

   





