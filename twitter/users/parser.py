from flask_restful import reqparse # 3yzen n-parse elrequest


post_parser = reqparse.RequestParser() # 3mlna object
user_parser = reqparse.RequestParser() #



# user_parser.add_argument('id', type=int, required=True, help='id is required')
user_parser.add_argument('username', type=str, required=True, help='username is required')
user_parser.add_argument('email', type=str, required=True, help='email is required')
user_parser.add_argument('image', type=str, required=True, help='image is required')
user_parser.add_argument('password', type=str, required=True, help='password is required')
