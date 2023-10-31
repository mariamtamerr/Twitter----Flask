from flask_restful import reqparse # 3yzen n-parse elrequest


post_parser = reqparse.RequestParser() # 3mlna object
user_parser = reqparse.RequestParser() #

# parse the title

# post_parser.add_argument('id', type=int, required=True, help='id is required')
post_parser.add_argument('title', type=str, required=True, help='title is required')
post_parser.add_argument('content', type=str, required=True, help='content is required')
post_parser.add_argument('user_id', type=int, required=True, help='id is required')
# post_parser.add_argument('date_posted', type=str, required=True, help='date is required')


user_parser.add_argument('id', type=int, required=True, help='id is required')
user_parser.add_argument('username', type=str, required=True, help='username is required')
