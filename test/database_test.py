# import pymongo
# from pymongo import MongoClient

# try:
#     myclient = MongoClient(
#         "mongodb+srv://prameus:transformers6@cluster0.eiyi4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#     db = myclient['serial_requester']
#     col = db['series']
#     some_dict = {
#         'ali': 'veli',
#         'muhammed': 'ali',
#         'amca': 'kaynana'}

#     # col.insert_one(some_dict)
#     # my_query = {'test': 'test'}

#     # col.delete_one(my_query)
#     # col.delete_many(some_dict)

#     print(myclient.list_database_names())
#     print(db.list_collection_names())

#     #! see collections inside
#     cursor = col.find({})
#     for document in cursor:
#         print(document)

# except Exception as e:
#     print(e)

some = ['aweawe', 'aweaweaw', 'aweaweawe', 'aweawewaeawe']

for i in some:
    print(i.index.__str__)
