def get_user(person):
    print(person.id)
    return person.id

def user_list(users):
    users.sort(key=get_user)
    return users

def get_report(users):
    for i in users:
        print(i.id, i.name, i.age)

class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

users = [
    Person("Ivan", 22, 2500),
    Person("Hark", 23, 2400),
    Person("Harold", 22, 2600),
    Person("Wert", 22, 2300)
]

list_users = user_list(users)
print(list_users)

get_report(list_users)
