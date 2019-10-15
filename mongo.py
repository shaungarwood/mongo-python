from pymongo import MongoClient
import datetime

client = MongoClient()
db = client['pymongo_test']
collection = db['stuff']

a = {
    'station': 'KUSA',
    'start': datetime.datetime.utcnow(),
    'question': "do you like ketchup?",
    'options': [
        'yes',
        'no',
        'mustard'
    ]

}

print("inserting")
collection.insert_one(a)
print("retrieving")
res = collection.find_one({'station': 'KUSA'})
print(res)
