from pymongo import MongoClient
import time

class Dataset:
    def __init__(self, url="mongodb://localhost:27017/", db_name="M2025A", collection_name="INFOs", action="Hold", Symbol="EURUSD=x", time=time.strftime('%Y-%m-%d %H:%M:%S'), ask = 0, st="Bollinger Bands", HT=0):
        self.Ok = False
        try:
            data = {
    "Model":"Model 2025 Alpha",
    "Symbol":Symbol,
    "Time":time,
    "Action":action,
    "Ask":ask,
    "Horizontal Touch":HT,
    "Strategy":st
            }
            # Create a MongoClient instance
            client = MongoClient(url)

            # Get a reference to the database and collection
            db = client[db_name]
            collection = db[collection_name]

            # Insert the data into the collection
            result = collection.insert_one(data)
            self.Ok = result.acknowledged

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Ensure the client connection is closed
            client.close()