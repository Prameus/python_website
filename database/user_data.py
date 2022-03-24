import random


class UsersData:
    all_chapter = '{all chapters data}'
    all_users = ['leluch vi britannia',
                 'golan trevize', 'hannibal', 'skyrim guard']
    users = []

    def watched(self):
        for user in self.all_users:
            for data in self.all_chapter:
                is_watched = dict(data=random.choice([True, False]))
            self.users.append({user: is_watched})


userdata = UsersData()
print(userdata.watched())
