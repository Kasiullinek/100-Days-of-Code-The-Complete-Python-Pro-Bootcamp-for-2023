class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Kate")
user_3 = User("003","Petra")

user_1.follow(user_3)
print(user_1.followers)
print(user_1.following)

print(user_3.followers)
print(user_3.following)

# user_2 = User()
# user_2.id = "002"
# user_2.name = "Jake"
#
# print(user_2.name)
