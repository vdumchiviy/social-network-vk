# import requests
from VKUser import VKUser


def main():
    user1 = VKUser(35163310)
    user2 = VKUser(2555015)

    friends = user1 & user2
    for friend in friends:
        friend.print_user_info()
    print(friends)
    print(user1)


main()
