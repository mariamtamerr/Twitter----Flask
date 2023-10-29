from flask_restful import reqparse # 3yzen n-parse elrequest


post_parser = reqparse.RequestParser() # 3mlna object

# parse the title
post_parser.add_argument('title', type=str, required=True, help='title is required')
 

