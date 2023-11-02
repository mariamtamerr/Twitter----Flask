
from flask_restful import Resource, fields, marshal_with , abort ##reosurce bta3 elserialization, fields from rest
from flask import make_response ## to return data
from twitter.models import Post, User, db
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

    
    
class PostResource(Resource):

    @marshal_with(post_serializer)
    def get(self, post_id):
        post = Post.get_specific_post(post_id)
        return post, 200


    @marshal_with(post_serializer)
    def put(self, post_id):
        post = Post.get_specific_post(post_id)
        if post:
            post_args = post_parser.parse_args()
            post.title=post_args["title"]
            post.content=post_args["content"]
            post.user_id=post_args["user_id"]
            db.session.add(post)
            db.session.commit()
            return post, 200
        abort(404, message="POst Object Not Found")
  


    def delete(self,post_id):
         post = Post.get_specific_post(post_id)
         if post:
             db.session.delete(post)
             db.session.commit()
             response = make_response("Deleted", 204)
             return response
         abort(404, message="Delete Object Not Found")

   




    
    
    
