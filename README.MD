# Task: Make a Class for social network vk.com (*\<be> in touch*) to helping access to user-profile and getting list of friends. Also, the class must be created in such a way that the execution of the "&" operation returns a list of class' objects referring to mutual friends

### Class VKUser
#### Description:
Method	  | Parameters | Return type|Description
:-------- |:-----:|:-----:|:-------
\_\_init__  | user_id:int  | -|Second method during Class creation
\_\_str__     | -    |_str_|string representation of the Class - link to the homepage of user
print_user_id      | user_id=None:int    |-| print user id with user = user_id (or current user if user_id is None)
get_user_info|user_id=None:int|_json_ of VK.users.get|get user description with with user = user_id (or current user if user_id is None)
print_user_info|user_id=None:int|-|print user information with user = user_id (or current user if user_id is None)  <user_id>: <first_name> <last_name>
get_friends|user_id=None:int|_set_ of VK id|return set with friends id of  user = user_id (or current user if user_id is None)
\_\_and__|other_VK_user:VKUser|_list_ of VKUser objects|overriding the "&" method. Method returns a list of class' objects referring to mutual friends current user and other_VK_user

#### Example of using:
```python
    user1 = VKUser(11111111)
    user2 = VKUser(22222222)

    friends = user1 & user2
    for friend in friends:
        friend.print_user_info()
    print(friends)
    print(user1)
```

