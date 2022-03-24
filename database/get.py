import json
import requests
import connection

response = requests.get('https://tv.kofteistan.co/')
data = response.json()
# print(data[2]['id'])  # id donduruyor
# print(data)

# print(data[1]) # 1. indexte bulunan diziyi donduruyor


# print(id)


# def pull_seasons():
#     count = 0
#     for chapters in data:
#         count += 1
#         print(f"{count}. season:{chapters}")
#     return data

class GetData:
    def pull_from_database(self):
        connection.connection_database.collection_content()

    def pull_chapters(self):
        all_serials = {}
        all_seasons = []

        for season in range(0, 3):
            # print(season)

            serial_name = data[season]['name']
            # print(serial_name)
            id = data[season]['id']
            # print(id)
            for chapter in range(1, 5):
                # print(chapter)
                another_response = requests.get(
                    f'https://tv.kofteistan.co/{id}/season/{chapter}').json()
                # print(f'data:{another_response}\n')

                all_seasons.append(another_response)
                # print(all_seasons)

            serial = {serial_name: all_seasons}
            all_serials.update(serial)
            all_seasons = []

        return all_serials


get_data = GetData()
#get_data.pull_chapters()
get_data.pull_from_database()
