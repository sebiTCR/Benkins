from flask import Blueprint, request

project_bp = Blueprint('project_bp', __name__)

@project_bp.route('/', methods=["GET", "POST", "DELETE"])
def project_methods():
    match request.method:
        case 'GET':
            #TODO: Get entry from database
            pass
        case 'POST':
            #TODO: Create a new project
            pass
        case "DELETE":
            #TODO: Remove a project
            pass
    return "unimplemented route"