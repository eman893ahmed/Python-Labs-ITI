def oreder_your_list_asc (user_list):
    return sorted(user_list)
    
def oreder_your_list_desc (user_list):
    return sorted(user_list, reverse=True)


user_list = input("Enter your list: ")
print("Your asecending list is :", oreder_your_list_asc(user_list))
print("Your desecending list is :", oreder_your_list_desc(user_list))
    
