
from flask_restful import Resource, fields, marshal_with  ##reosurce bta3 elserialization, fields from rest
from flask import make_response ## to return data
from twitter.models import Post, User
from twitter.posts.parser import post_parser, user_parser
# from twitter import db 



# API 3 PARTS :

# 1)  RECEIVE DATA 




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


# 3) CRUD OPERATIONS  

class PostList(Resource):

    @marshal_with(post_serializer)
    def get(self):
        posts = Post.query.all() #get all posts objects
        return posts, 200 
    


# ------- FOR THE POST METHOD --------------------
  # 1- Get Data From Form :
            # Parse Form Data You Got From Application
            # Give It To Function To Create Object
            # So You Must Create The Parser File
    # 2- Save & Return Result 
    @marshal_with(post_serializer)
    def post(self):
        post_args = post_parser.parse_args() # it will take data gyalak fl post w ytabba2 3aleha
        print(post_args)
        post = Post.create_post(post_args)
        print("this is post : " , post)
        return post, 201 
        # if 'id' in post_args:
        #     del post_args['id']
        #     post = Post.create_post(post_args)
        # if post:
        #     print("post created:", post)
        #     return post, 201
        # else:
        #     print("post creation failed")
        #     return {"message": "post creation failed"}, 500

    
    

        # return 'added posts through post method'

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
        user_args = user_parser.parse_args()
        print("Received user_args:", user_args)
        user = User.create_user(**user_args)
        if user:
            print("User created:", user)
            return user, 201
        else:
            print("User creation failed")
            return {"message": "User creation failed"}, 500

    
    
    
    
    
