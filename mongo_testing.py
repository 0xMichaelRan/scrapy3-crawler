import pymongo
from bson.objectid import ObjectId

connection = pymongo.MongoClient('128.199.103.166', 27017)
db = connection.online_groc
items = db.bigtable

# search based on keywords
print 'so.. the list of items: '
for item in items.find({ 
		'brand': { '$regex' :".*MARIGOLD.*"}, 
		'title': { '$regex' :".*Milk.*"}
	}):
    print str(item['_id']) + ' - '  + item['brand'] + ', '  + item['title']

# search one item by ID
oneItem = items.find_one({
		'_id': ObjectId('5581127c5c7c67ffb8bdfc05')
	})

print 'so.. the one item is: '
print str(oneItem['_id']) + ' - '  + oneItem['brand'] + ', '  + oneItem['title']
