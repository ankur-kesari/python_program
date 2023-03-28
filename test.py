import boto3
import json
import urllib.parse
import pymongo
from pymongo import MongoClient


def lambda_handler(event, context):
    # create a Secrets Manager client
    client = boto3.client('secretsmanager')

    # retrieve the secret value for a specific secret
    response = client.get_secret_value(SecretId='test')

    # extract the secret string from the response
    secret_string = response['SecretString']

    # parse the secret string as a JSON object
    secret_dict = json.loads(secret_string)
    mongo_url  = secret_dict['mongo_url']

    # print the secret value
    print(mongo_url)
    
     # extract the MongoDB connection string from the event
    connection_string = mongo_url

    # parse the connection string with urllib.parse
    parsed_uri = urllib.parse.urlparse(connection_string)

    # extract the username and password from the parsed URI
    username = urllib.parse.unquote(parsed_uri.username)
    password = urllib.parse.unquote(parsed_uri.password)

    # print the username and password
    print("Username: " + username)
    print("Password: " + password)
    
    
    # connect to the MongoDB database
    
    client1 = pymongo.MongoClient(mongo_url)
     
    print(client1)

    # return the client object
    # return client
    
    db = client1.get_database()
    
    # db = MongoClient(mongo_url).get_database()
    # print(db.name)
    
    print(db)
    
    # db = client["SmartEditorDB"]
    # users = db["users"]
        
    # print(users)
    
    # # find user by username
    # user = users.find_one({"username": "FreeFuseStagingDB"})
    
    # print(user)
    
    # # update user password
    # users.update_one({"username": "FreeFuseStagingDB"}, {"$set": {"password": "newpasswordtest@"}})
    
    # print("Password updated for user", user["username"])
    
    
    
    
    
    
    
    
    
    
    
    
# def connect_to_atlas():
#     # Set up connection parameters
#     username = "FreeFuseStagingDB"
#     password = ""
#     cluster_endpoint = "cluster0.5h6nr.mongodb.net"

#     # Construct connection string
#     connection_string = f"mongodb+srv://{username}:{password}@{cluster_endpoint}/test?retryWrites=true&w=majority"

#     # Connect to MongoDB Atlas
#     client = pymongo.MongoClient(connection_string)

#     # Return the client object
#     return client    
