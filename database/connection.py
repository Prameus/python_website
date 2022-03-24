from pymongo import MongoClient
import get


class Connection:
    myclient = MongoClient(
        "mongodb+srv://prameus:transformers6@cluster0.eiyi4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = myclient['serial_requester']
    series_col = db['series']
    users_col = db['users']

    def collection_content(self):
        # #! see collections inside
        cursor = self.series_col.find()
        for document in cursor:
            print(document)
        # print(self.myclient.list_database_names())
        # print(self.db.list_collection_names())

    def get_data(self):
        avatar = []
        doctor_who = []
        good_omens = []

        series = get.get_data.pull_chapters()
        for serial in series:
            for season in range(0, 4):
                chapters = series[serial][season]

                if chapters != "{'detail': 'Not Found'}":
                    if serial == 'Avatar: The Last Airbender':
                        avatar.append(chapters)
                    elif serial == 'Doctor Who':
                        doctor_who.append(chapters)
                    elif serial == 'Good Omens':
                        good_omens.append(chapters)
        # self.series_col.insert_one({"'Avatar: The Last Airbender'": avatar})
        # self.series_col.insert_one({"'Doctor Who'": doctor_who})
        # # self.series_col.insert_one({"'Good Omens'": good_omens})
        # avatar_id = "'_id': ObjectId('623b0b8be127de7857096164'}"
        # self.series_col.update_one(avatar_id, { "$set" ,avatar})
        # self.series_col.update_one(
        #     {"'_id': ObjectId('623b0b8be127de7857096165')"}, doctor_who)
        # self.series_col.update_one(
        #     {"'_id': ObjectId('623b0b8be127de7857096166')"}, good_omens)

    def pull_from_database(self):
        pass


connection_database = Connection()
connection_database.collection_content()
# connection.get_data()
