#  import statements
import pymongo
import pandas as pd
import json

class MongoDBManagement:
    def __init__(self, username, password):
        """
        this function create required connection url for further process.
        
        Parameters
        ----------
        username: str
            username of mongodb collection
        password: str
            password of monogodb collection
        """
        try:
            self.username = username
            self.password = password
            self.url = "mongodb+srv://{}:{}@firstcluster.zkbe8zb.mongodb.net/?retryWrites=true&w=majority".format(self.username,self.password)
            
        except Exception as e:
            raise Exception(f"(__init__): not able to initiate mongodburl. Error: {str(e)}")
            
    def getMongoDBclientObject(self):
        """
        this function will create client connection object for mongodb server.
        
        Parameters
        ----------
        Null
        
        Return
        ----------
        mongo_client: connection object
            you can use this object to run any query in mongodb.
        """
        try:
            mongo_client = pymongo.MongoClient(self.url)
            return mongo_client
        except Exception as e:
            raise Exception(f"(getMongoDbclientObject): Not able to create client object. Error: {str(e)}")
        
    def closeMongoDBconnection(self, mongo_client):
        """
        this function close the connection of client with server.
        
        Parameters
        ----------
        mongo_client: connection object
        
        Return
        ----------
        Null
        """
        try:
            mongo_client.close()
        except Exception as e:
            raise Exception(f"something went wrong on closing connection. Error: {str(e)}")
            
    def isDatabasePresent(self, db_name):
        """
        this function will check if database you are trying to use is already in db or not.
        
        Parameters:
        -----------
        db_name : str
            database name you want to check
        
        Returns:
        -----------
        status : True/False
        """
        try:
            mongo_client = self.getMongoDBclientObject()
            if db_name in mongo_client.list_database_names():
                mongo_client.close()
                return True
            else:
                mongo_client.close()
                return False
        except Exception as e:
            raise Exception(f"(isDatabasePresent): failed to check database existence. Error: {str(e)}")
    
    def createDatabase(self, db_name):
        """
        this function will create database in mongodb.
        Inside it wil automatically check existence of database.
        
        Parameters:
        -----------
        db_name : str
            database name with which you want to create db.
            
        Returns:
        ----------
        database : database object 
        """
        try:
            mongo_client = self.getMongoDBclientObject()
            database = mongo_client[db_name]
            mongo_client.close()
            return database
        except Exception as e:
            raise Exception(f"(): failed to create database. Error: {str(e)}")