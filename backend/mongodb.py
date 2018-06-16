from pymongo import MongoClient
from bson.objectid import ObjectId


class MongoDatabase():
    """
    Database class for storing wine info

    Currently using MongoDB for flexibility with schema

    TODO: Make a generice interface so that different DBs can be supported
    """

    """
    wine info:
    year (int)
    Type (string)
    Brand/Winery (string)
    Quantity (int)
    Notes (string)
    Tags (list)
    """
    def __init__(self, host='localhost', port=27017, username=None, password=None):
        """
        Initializes the DB object

        :param host: host to connect to (str)
        :param port: port to connect to (int)
        :param username: login username (str)
        :param password: login password (str)
        """
        if username is None:
            self.client = MongoClient('{0}:{1}'.format(host, port))
            self.database = None
            self.collection = None
            self.wine_list = None

    def set_db(self, dbname='wine_list'):
        """
        Sets the DB to use

        :param dbname: database to use
        """
        self.database = self.client.get_database(dbname)

    def set_collection(self, collection_name='wine_list'):
        """
        Sets collection to use

        :param collection_name: collection name to use
        """
        self.collection = self.database.get_collection(collection_name)

    def refresh_list(self):
        """
        Refreshes wine_list by loading contents from DB
        """
        latest_wine_list = []
        for wine in self.collection.find():
            wine['_id'] = str(wine['_id'])
            latest_wine_list.append(wine)
        self.wine_list = latest_wine_list

    def insert(self, data):
        """
        Inserts data into DB

        :param data: wine info in dict form to insert (dict)
        """
        try:
            self.collection.insert_one(data)
            return True
        except Exception as e:
            print(str(e))
            return False

    def find(self, id):
        """
        Returns wine info with supplied id

        :param id: a unique identifier (str)
        :return: wine info (json) or None
        """
        try:
            for wine in self.wine_list:
                if wine['_id'] == id:
                    return wine
            else:
                return None
        except Exception as e:
            print(str(e))

    def update(self, id, data):
        """
        Updates the wine identified by id with the data

        :param id: unique identifier for wine (str)
        :param data: data to update in json form (json)
        """
        try:
            self.collection.update_one(
                {'_id': ObjectId(id)},
                {"$set": data})
            return True
        except Exception as e:
            print(str(e))
            return False

    def delete(self, id):
        """
        Deletes item from DB based on id supplied

        :param id: ID of record (str)
        :return: Whether or not delete was successful (bool)
        """
        try:
            self.collection.delete_one({'_id': ObjectId(id)})
            return True
        except Exception as e:
            print('Deletion of record identified by {0} failed: {1}'.format(id, str(e)))
            return False

