"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os, json
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
jackson_family = FamilyStructure('Jackson')

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return jsonify(response_body), 200

@app.route('/descendants/<int:id>')
def get_descendants(id):
    descendants = jackson_family.get_all_descendants(id)
    return jsonify(descendants), 200

@app.route('/ancestors/<int:id>')
def get_ancestors(id):
    ancestors = jackson_family.get_ancestors(id)
    return jsonify(ancestors), 200    

@app.route('/siblings/<int:id>')
def get_siblings(id):
    siblings = jackson_family.get_siblings(id)
    return jsonify(siblings), 200        

@app.route('/member', methods=['POST'])
def post_member():
    member = request.json        
    jackson_family.add_member(member)
    members = jackson_family.get_all_members()   
    response = {
        "status": "Family member posted with id",
        "family": members
    } 
    return jsonify(response), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(id)
    return jsonify(member), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.delete_member(id)
    print("Deleted member: ", member)
    family = jackson_family.get_all_members()
    response_body = {
        "deleted": member,
        "family": family
    }
    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
