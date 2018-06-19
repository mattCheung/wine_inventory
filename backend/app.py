import json
from flask import abort, Flask, make_response,request, url_for
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource, reqparse, fields
from mongodb import MongoDatabase

"""
/wine_list/v1.0/wines
/wine_list/v1.0/wines/{id}
"""

app = Flask(__name__, static_url_path='')
api = Api(app)

wine_fields = {
    'id': fields.Integer,
    'type': fields.String,
    'brand': fields.String,
    'year': fields.Integer,
    'quantity': fields.Integer,
    'notes': fields.String,
    'tags': fields.List
}

wine_list_mongo = MongoDatabase()
wine_list_mongo.set_db()
wine_list_mongo.set_collection()
wine_list_mongo.refresh_list()


class WineListAPI(Resource):
    """
    Manipulating the actual wine list
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('year', type=int, required=True, help='No year provided'
                                   , location='json')
        self.reqparse.add_argument('type', type=str, required=True, help='No type provided'
                                   , location='json')
        self.reqparse.add_argument('winery', type=str, required=True, help='No winery provided',
                                   location='json')
        self.reqparse.add_argument('name', type=str, required=False, location='json')
        self.reqparse.add_argument('quantity', type=str, required=False, location='json', default=1)
        self.reqparse.add_argument('notes', type=str, required=False, location='json', default='')
        self.reqparse.add_argument('tags', type=list, required=False, location='json', default=[])
        super().__init__()

    def get(self):
        """
        Gets the current wine list from memory
        :return: List of wines (list)
        """
        # curl -i http://localhost:5000/wine_list/api/v1.0/winelist
        wine_list_mongo.refresh_list()
        response = make_response(json.dumps({'wine':
                                                 [self.make_public_wine(wine) for wine in
                                                  wine_list_mongo.wine_list]}), 200
                                 , {'Access-Control-Allow-Origin': '*'})
        return response

    def make_public_wine(self, wineInfo):
        new_wine = {}
        for field in wineInfo:
            if field == '_id':
                new_wine['_id'] = wineInfo['_id']
                new_wine['uri'] = url_for('winelist', task_id=wineInfo['_id'], _external=True)
            else:
                new_wine[field] = wineInfo[field]
        return new_wine

    def post(self):
        """
        Creates new wine record in DB with data from json via reqparse

        :return: Whether insert was successful or not
        """
        # curl -i -H "Content-Type: application/json" -X POST -d '{"year": 1996, "type": "experimental", "winery": "no name", "name": "experiment"}' http://localhost:5000/wine_list/api/v1.0/winelist
        args = self.reqparse.parse_args()
        wine = {
            'year': args['year'],
            'type': args['type'],
            'winery': args['winery'],
            'name': args['name'],
            'quantity': args['quantity'],
            'notes': args['notes'],
            'tags': args['tags']
        }
        if wine_list_mongo.insert(wine):
            wine['_id'] = str(wine['_id'])
            response = make_response(json.dumps({'wine': wine}), 201)
            return response
        else:
            return make_response(json.dumps({'error': 'unknown error'}), 400)

class WineAPI(Resource):
    """
    Manipulating the actual wine info
    """
    def __init__(self):
        """
        Initializes the object, sets up parser
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('quantity', type = str, required = False, location = 'json')
        self.reqparse.add_argument('notes', type = str, required = False, location = 'json')
        self.reqparse.add_argument('tags', type = list, required = False, location = 'json')
        super().__init__()

    def get(self, id):
        """
        Gets the specific info for a wine identified by the ID

        :param id: ID of wine (str)
        :return: Info about the wine if found (dict)
        """
        # curl -i http://localhost:5000/wine_list/api/v1.0/winelist
        wine_list_mongo.refresh_list()
        for wine in wine_list_mongo.wine_list:
            if wine['_id'] == id:
                response = make_response(json.dumps({'wine': wine}), 200
                , {'Access-Control-Allow-Origin': '*'})
                return response
        abort(404)

    def patch(self, id):
        """
        Updates specific info for the wine (as supplied by argparse via json)

        :param id: ID of the wine to update
        :return: Updated wine info (json)
        """
        # curl -i -H "Content-Type: application/json" -X PATCH -d '{"quantity": 99}' http://localhost:5000/wine_list/api/v1.0/winelist/5b22f0748245f81401b68553
        for wine in wine_list_mongo.wine_list:
            if wine['_id'] == id:
                print('updating {0} with {1}'.format(id, request.json))
                wine_list_mongo.update(id, request.json)
                break
        else:
            abort(404)

        print('updating')
        wine_list_mongo.refresh_list()
        for wine in wine_list_mongo.wine_list:
            if wine['_id'] == id:
                print('returning {0}'.format(wine))
                response = make_response(json.dumps({'wine': wine}), 200)
                return response

    def put(self, id):
        pass

    def delete(self, id):
        """
        Deletes wine specified by ID from DB

        :param id: ID of wine to delete (str)
        :return: Whether or not the deletion was successful
        """
        # curl -i -X DELETE http://localhost:5000/wine_list/api/v1.0/winelist/5b22f0748245f81401b68553
        for wine in wine_list_mongo.wine_list:
            if wine['_id'] == id:
                print('calling delete')
                wine_list_mongo.delete(id)
                response = make_response(json.dumps({'result': True}), 200)
                return response
        abort(404)

api.add_resource(WineListAPI, '/wine_list/api/v1.0/winelist', endpoint='winelist')
api.add_resource(WineAPI, '/wine_list/api/v1.0/winelist/<string:id>', endpoint = 'wine')

if __name__ == '__main__':
    app.run(debug=True)
