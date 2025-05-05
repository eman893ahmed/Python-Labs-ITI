def find_i_in_str(str):

    for i in range(len(str)):
        if str[i] == "i":
            
            return i

str = input("Enter your string to find i's: ")
print("Location of i is: ",find_i_in_str(str))
