username_list = []

def authorization (username):

    while not username.isalpha():
        return 0

   
    else:
        return 1

username = input( "Enter your username with no spcaes or numbers: " )

if(authorization(username)) == 0:
        print( "Invalid username" )
else:
        useremail = input( "Enter your e-mail: " )
        username_list.append(username)
        username_list.append(useremail)
        print(username_list)

