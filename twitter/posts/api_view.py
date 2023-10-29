
from flask_restful import Resource, fields, marshal_with  ##reosurce bta3 elserialization, fields from rest
from flask import make_response ## to return data
from twitter.models import Post, User
# from twitter import db 



# API 3 PARTS :

# 1)  RECEIVE DATA 




# 2) SERIALIZATION OF DATA

post_serializer = {
    "id": fields.Integer,
    "title": fields.String,
    "content": fields.String

}


user_serializer = {
    "id": fields.Integer,
    "username": fields.String,
    "posts": fields.Nested(post_serializer)
}


# 3) CRUD OPERATIONS  

class PostList(Resource):

    @marshal_with(post_serializer)
    def get(self):
        posts = Post.query.all() #get all posts objects
        return posts, 200 
    

    # def post(self, request): 
    

class UserList(Resource):

    @marshal_with(user_serializer)
    def get(self):
        users = User.query.all() #get all users objects
        return users, 200 
    
    @marshal_with(user_serializer)
    def post(self):
        pass
    # 1- Get Data From Form :
            # Parse Form Data You Got From Application
            # Give It To Function To Create Object
            # So You Must Create The Parser File
    # 2- Save & Return Result 
    
    
    
    
    
    
