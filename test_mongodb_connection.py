from pymongo import MongoClient
client = MongoClient("<mongodb_url_string>")
db = client.admin
try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
# client.close()


# db =  client.admin
col = db["system.users"]



total_docs = col.count_documents({})
print (col.name, "has", total_docs, "total documents.")

client.close()
