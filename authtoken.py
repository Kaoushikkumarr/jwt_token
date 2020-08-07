# Generating the JWT token which will be invalid after every 50 sec
# from the time of generation and then new to generate new unique token once again

import datetime
from functools import wraps
from flask_restful import Resource, Api
from flask import Flask, render_template, request, jsonify, make_response
import jwt

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'thisissecretkey'


def check_for_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'Missing Token'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])

        except:
            return jsonify({'message': 'Invalid token'})

        return f(*args, **kwargs)

    return decorated


#
# class Unsecure(Resource):
#     # @app.route('/unprotected')
#     def get(self):
#         return jsonify({'message': 'No need of token.'})
#

class Secure(Resource):

    @check_for_token
    def get(self):
        return jsonify({'message': 'Login Success.'})


class Login(Resource):

    def get(self):
        auth = request.authorization
        if auth and auth.password == 'password':
            token = jwt.encode(
                {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)},
                app.config['SECRET_KEY'])

            return jsonify({'token': token.decode('UTF-8')})

        return make_response("Invalid User Credentials", 401, {'Authenticate': 'Login Required'})


api.add_resource(Login, '/login', methods=['GET'])
api.add_resource(Secure, '/secure', methods=['GET'])
# api.add_resource(Unsecure, '/unsecure', methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
