from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from core.bootstrap import Bootstrap
from routes.attendance_routes import attendance_routes

load_dotenv()

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, resources={
    r'/*': {
        'origins': [
            'http://localhost:3001'
        ]
    }
})


app.register_blueprint(attendance_routes)

if __name__ == "__main__":
    Bootstrap()
    app.run(host="0.0.0.0", debug=True, port=5002)
