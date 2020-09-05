import requests


class VKUser:
    TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"
    VKAPI_URL = "https://api.vk.com/method/"

    def __init__(self, user_id):
        '''Second method during Class creation'''
        self.user_id = user_id

    def __str__(self):
        '''string representation of the Class - link to the homepage of user'''
        return f"https://vk.com/id{str(self.user_id)}"

    def print_user_id(self, user_id=None):
        '''print user id with user = user_id (or current user if user_id is None)'''
        print(f"User id is {self.user_id if user_id is None else user_id}")

    def get_user_info(self, user_id=None):
        '''get user description with with user = user_id (or current user if user_id is None)'''
        parameters = {"access_token": self.TOKEN,
                      "user_ids": self.user_id if user_id is None else user_id,
                      "v": "5.122"}
        response = requests.get(url=self.VKAPI_URL +
                                "users.get", params=parameters)
        return response.json()

    def print_user_info(self, user_id=None):
        '''print user information with user = user_id (or current user if user_id is None)
        <user_id>: <first_name> <last_name>'''
        user_info = self.get_user_info(
            self.user_id if user_id is None else user_id)
        print(
            f"{user_info['response'][0]['id']}: {user_info['response'][0]['first_name']} {user_info['response'][0]['last_name']}")

    def get_friends(self, user_id=None):
        '''return set with friends id of  user = user_id (or current user if user_id is None)'''
        parameters = {"access_token": self.TOKEN,
                      "user_id": self.user_id if user_id is None else user_id,
                      "v": "5.122"}
        response = requests.get(url=self.VKAPI_URL +
                                "friends.get", params=parameters)
        return set(response.json()["response"]["items"])

    def __and__(self, other_VK_user):
        '''overriding the "&" method. Method returns a list of class' objects referring to mutual friends current user and other_VK_user'''
        common_friends = list()
        friends = self.get_friends() & other_VK_user.get_friends()

        for friend in friends:
            common_friends.append(VKUser(friend))
        return common_friends


if __name__ == '__main__':

    user1 = VKUser(35163310)
    user2 = VKUser(2555015)

    friends = user1 & user2
    for friend in friends:
        friend.print_user_info()
    print(friends)
    print(user1)
