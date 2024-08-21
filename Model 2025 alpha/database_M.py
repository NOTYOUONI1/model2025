import time as tm
from pymongo import MongoClient

class MongoDB():
    def __init__(self, url, db_name):
        self.url = url
        self.db_name = db_name
        self.client = MongoClient(self.url)
        self.db = self.client[self.db_name]
    
    def insert_data(self, data, col):
        # Add a timestamp to the data
        data["time"] = tm.strftime('%Y-%m-%d %H:%M:%S')
        
        # Get the collection
        collection = self.db[col]
        
        # Insert the data into the collection
        result = collection.insert_one(data)
        
        # Return whether the insertion was acknowledged and the inserted ID
        return result.acknowledged, result.inserted_id
    
    def update_data(self, old_data, new_data, col):
        # Add a timestamp to the new data        
        new_data["time"] = tm.strftime('%Y-%m-%d %H:%M:%S')
        collection = self.db[col]
        
        # Perform the update
        result = collection.update_one(old_data, {"$set": new_data})
        
        # Return whether the update was acknowledged and the number of documents updated
        return result.acknowledged, result.modified_count
    def find_data(self, col):
    # Get the collection
        collection = self.db[col]
    
    # Find a single document matching the query
        document = collection.find()
        document = list(document)
    
        return document