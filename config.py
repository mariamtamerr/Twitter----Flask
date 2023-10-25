
import os
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY



class Config:
  
    # SECRET_KEY=os.environ.get('SECRET_KEY')   #python --> import secrets --> secrets.token_hex(16)
    # SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_TRACK_MODIFICATIONS=False ###### for the ap.context

    # IPYHON_CONFIG = {
    #     'InteractiveShell': {
    #         'colors': 'Linux',
    #         'confirm_exit': False,
    #     },
    # }


    SECRET_KEY='13992d730c4efd613a11ed4b6a65e51c'   #python --> import secrets --> secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db' # 3 slashes for the relative path
    SQLALCHEMY_TRACK_MODIFICATIONS=False ###### for the ap.context

    IPYHON_CONFIG = {
            'InteractiveShell': {
                'colors': 'Linux',
                'confirm_exit': False,
            },
        }






