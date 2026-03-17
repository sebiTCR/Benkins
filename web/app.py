from flask import Flask, url_for
from blueprints.project import project_bp

app = Flask(__name__)

app.register_blueprint(project_bp,  url_prefix="/project")

@app.route('/')
def root():
    return "Benkins!"