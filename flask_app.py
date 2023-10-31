
from twitter import app 
import os

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0')
    # os.system('gunicorn -c gunicorn_config.py twitter:app')
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)


    