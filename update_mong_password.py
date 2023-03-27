#Both program not working to update existing user password

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('<mongo_url_string>')

# # Get the database and user collection
# db = client['mydatabase']
# users = db['admin']

# # Define the new password for the user
# new_password = 'nfaghshikdn1dagh'

# # Update the user's password
# users.update_user(
#     'admin',
#     password=new_password,
#     mechanism='SCRAM-SHA-256'
# )
db = client.get_database()
print(db)

############################################

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongo_url_string')

# Get the database and user collection
db = client['mydatabase']
users = db['admin']

# Define the new password for the user
new_password = 'nfaghshikdn1dagh'

# Update the user's password
#users.update_user(
#    "admin",
#    password=new_password,
#    mechanism='SCRAM-SHA-256'
#)

db.command( { updateUser: "admin",
 pwd: "hgaerfgyu123asdfh",
 roles: [
  "readWrite"
 ]
})
