'''
Joe Kurtz
11/22/21
'''
import datetime
d = datetime.datetime.now()
month = str(d.month)
day = str(d.day)
year = str(d.year)
hour = str(d.hour)
minute = str(d.minute)
second = str(d.second)

import random

# function:   valid_username
# input:      a username (string)
# processing: determines if the username supplied is valid.  for the purpose
#             of this program a valid username is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) the first character cannot be a number
# output:     boolean (True if valid, False if invalid)

def valid_username(x):

    valid = True

    # Determine if NOT Valid
    if len(x) < 5:
        valid = False
    elif x.isalnum() == False:
        valid = False
    elif x[0].isnumeric():
        valid = False

    # Return BOOL value for Username
    return valid

# function:   valid_password
# input:      a password (string)
# processing: determines if the password supplied is valid.  for the purpose
#             of this program a valid password is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) must contain at least one lowercase letter
#             (4) must contain at least one uppercase letter
#             (5) must contain at least one number
# output:     boolean (True if valid, False if invalid)

def valid_password(x):

    valid = True

    if len(x) < 5:
        valid = False
    elif x.isalnum() == False:
        valid = False

    # Count LOWER, UPPER, NUM
    lower = 0
    upper = 0
    num = 0
    for c in x:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        elif c.isnumeric():
            num += 1

    if lower == 0:
        valid = False
    elif upper == 0:
        valid = False
    elif num == 0:
        valid = False

    return valid

# function:   username_exists
# input:      a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:     boolean (True if found, False if not found)

def username_exists(x):
    exists = False

    # Open File 'user_info.txt' in Read mode
    # Bring in ALL Data
    # Close File
    file_object = open("user_info.txt","r")
    data = file_object.read()
    file_object.close()

    # Split Data into List Seperated by "\n"
    lists = data.split("\n")

    # Now, Seperate Each Index in List by ","
    for p in lists:
        pair = p.split(",")

        # Now Check if Username Exists in "pair[0]"
        if x == pair[0]:
            exists = True

        # Condition for Empty String
        if len(x) == 0:
            exists = False

    return exists

# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)

def check_password(user,password):

    valid = False
    
    # Open File 'user_info.txt' in Read mode
    # Bring in ALL Data
    # Close File
    file_object = open("user_info.txt","r")
    data = file_object.read()
    file_object.close()

    # Split Data into List Seperated by "\n"
    lists = data.split("\n")

    # Now, Seperate Each Index in List by ","
    for p in lists:
        pair = p.split(",")

        if user == pair[0] and password == pair[-1]:
            valid = True

        if len(user) == 0 or len(password) == 0:
            valid = False

    return valid

# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given users
#             with the following information:
#
#             sender|date_and_time|message\n
#
#             for example, if you call this function using the following arguments:
#
#             send_message('craig', 'pikachu', 'Hello there! nice to see you!')
#
#             the file 'messages/pikachu.txt' should gain an additional line data
#             that looks like the following:
#
#             craig|11/14/2020 12:30:05|Hello there! nice to see you!\n
#
#             note that you can generate the current time by doing the following:
#
#             import datetime
#             d = datetime.datetime.now()
#             month = d.month
#             day = d.day
#             year = d.year
#             ... etc. for hour, minute and second
#
#             keep in mind that you may need to 'append' to the correct messages file
#             since a user can receive an unlimited number of messages.  you may also
#             need to create a new message file if one does not exist for a user.
# output:     nothing

def send_message(s,r,m):

    # Open File Based on "r"
    # ... Append "m" to File from "s"
    # ... Timestamp Each Message month/day/year hour:minute:second
    file_object = open(f"messages/{r}.txt","a")
    file_object.write(s+ "|")
    file_object.write(month+"/"+day+"/"+year +" ")
    file_object.write(hour+":"+minute+":"+second +"|")
    file_object.write(m + "\n")
    file_object.close()



# function:   add_user
# input:      a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output:     boolean (True if added successfully, False if not)

def add_user(user, p):
    valid_new = True
    already_added = []

    # Open File 'user_info.txt' in Append mode
    # Bring in ALL Data

    file_object = open("user_info.txt","r")
    data = file_object.read()
    file_object.close()

    # Datermine if Username Already Exists    # Split Data into List Seperated by "\n"
    lists = data.split("\n")

    # Now, Seperate Each Index in List by ","
    for i in lists:
        already_added += [i.split(",")[0]]

    if user not in already_added:
        file_object = open("user_info.txt","a")
        file_object.write(user +","+p+"\n")
        new_message = send_message("admin",user,"Welcome to your account!")
        already_added += [user]
    else:
        valid_new = False

    return valid_new

# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.  assume you have this file named 'charmander.txt':
#
#             pikachu|11/14/2020 13:37:15|Hey there!
#             pikachu|11/14/2020 13:37:15|You too, ttyl
#
#             this function should generate the following output:
#
#             Message #1 received from pikachu
#             Time: 11/14/2020 13:37:15
#             Hey there!
#
#             Message #2 received from pikachu
#             Time: 11/14/2020 13:37:15
#             You too, ttyl
# output:     no return value (simply prints the messages)

def print_messages(u):

    # Open "messages/{u}.txt" file in "r" Mode
    # ... Extract All Data from File
    # ... Convert Data into List
    # ... Close File
    file_object = open(f"messages/{u}.txt","r")
    data = file_object.read()
    file_object.close()

    # Split Data Among "\n" Character
    data_list = data.split("\n")


    # Now, Each Individual Message is a Single Index

    # Now for Each Index in "data_list"
    # ... Split Among "|" Character
    new_list = []
    message_num = 1
    for s in data_list:
        if len(s) > 0:
            messages = s.split("|")


            # Now Print Out Output
            print(f"Message #{message_num} received from {messages[0]}")
            print(f"Time: {messages[1][:11]}{messages[1][11:]}")
            print(f"{messages[-1]}")
            print()

            message_num += 1

def print_messages_count(u):

    # Open "messages/{u}.txt" file in "r" Mode
    # ... Extract All Data from File
    # ... Convert Data into List
    # ... Close File
    file_object = open(f"messages/{u}.txt","r")
    data = file_object.read()
    file_object.close()

    # Split Data Among "\n" Character
    data_list = data.split("\n")


    # Now, Each Individual Message is a Single Index

    # Now for Each Index in "data_list"
    # ... Split Among "|" Character
    new_list = []
    message_num = 1
    for s in data_list:
        if len(s) > 0:
            messages = s.split("|")


            message_num += 1

    return message_num



# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value
def delete_messages(user):

    # Open User Txt File "messages/{user}.txt" in "w" Mode
    # Edit the Existing Text in there by Calling ".write()"
    # Close File Once it is Empty
    file_object = open(f"messages/{user}.txt","w")
    file_object.close()

def ascii_shift(word, i):

    new_word = ""
    for c in word:

        new_c = chr((ord(c)+ i))
        new_word += new_c


    return new_word

def shift_right(word):

    # Condition for Empty String
    if len(word) == 0:
        return word

    # Otherwise, Return Word Shifted to Right
    else:
        new_word = word[-1] + word[0:-1]
        return new_word

def shift_left(word):

    # Provision if Empty String
    if len(word) == 0:
        return word
    
    else:

        # New Word = Old Word Index [1, End] + Index [0]
        new_word = word[1:] + word[0]
        return new_word
    
def flip(word):

    # Provision if Empty String
    if len(word) == 0:
        return word

    else:

        # If Word is Even
        if len(word) % 2 == 0:

            # Take Second Half of Word - [len(word) / 2 : End]

            new_word = word[(len(word) // 2):] + word[:(len(word)//2)]
            return new_word

        # Else, Word is Odd
        else:

            # Keep Middle Letter
            # Flip Second Half with First Half

            new_word = word[(len(word) // 2) + 1 : ] + word[(len(word) // 2)] +  word[:(len(word) // 2)]
            return new_word


def add_letters(word, num):
    

    new_word = ""

    
    # Add Random Amount of Letters Between Characters
    for c in word:

        # Call Random Integers
        # Convert Integer to Character

        # If Letter Beforehand Contained Same Letter
        # ... Redraw Character
        # Add Character to String

        random_c = chr(random.randint(65,90))


        new_word += c

        for i in range(num):

            if new_word[-1] == random_c:
                random_c = chr(random.randint(65,90))
                new_word += random_c
            else:
                new_word += random_c

    return new_word

def delete_characters(word, num):

    # Creat New Word Empty String
    new_word = word[0]
    
    # Keep Character [0]
    # Remove Next "num" characters

    # For Every Character ("c") in "word"
    #               0: End of Word : Skip By Skip Counter
    for c in word[1:(len(word)+1):(num+1)]:

        # Add Character to Empty String
        new_word += c

    # Return "new_word"
    return new_word

def decode_message(user,num,key):
    file_object = open(f"messages/{user}.txt","r")
    data = file_object.read()
    file_object.close()

    # Break it Up By Message, Then by "|"
    messages = data.split("\n")

    count = 0
    message_list = []
    for m in messages:

        if len(m) > 0:
            message = m.split("|")
            message_list += [message]
            count += 1

    new_word = message_list[num-1][-1]
    for c in key:

        # If User Inputted "A" --> Call "add_letters"
        if c == "A":
                
            current_word = add_letters(new_word,1)

            new_word = current_word


        elif c == "X":

            current_word = delete_characters(new_word,1)
            new_word = current_word
            
        elif c == "F":
            current_word = flip(new_word)
            new_word = current_word

        elif c == "U":
            current_word = ascii_shift(new_word,1)
            new_word = current_word
            
        elif c == "D":
            current_word = ascii_shift(new_word,-1)
            new_word = current_word
      
        elif c == "L":
            current_word = shift_left(new_word)
            new_word = current_word
            
        elif c == "R":
            current_word = shift_right(new_word)
            new_word = current_word

    
    
    return new_word

# decode_message("user1",2,"XXX")
'''
LIST OF FUNCTIONS (For Reference):
(1) valid_username
(2) valid_password
(3) username_exists
(4) check_password
(5) add_user
(6) send_message
(7) print_messages
(8) delete_messages
(15) decode_message

(9) ascii_shift
(10) shift_right
(11) shift_left
(12) flip
(13) add_letters
(14) delete_characters
'''

while True:

    command = str.upper(input("(l)ogin, (r)egister or (q)uit: "))
    print()

    while command not in "LRQ":
        print("Invalid Command, Try Again!")
        print()
        command = str.upper(input("(l)ogin, (r)egister or (q)uit: "))

    # IF "command" == "R", Prompt User:
    # ... Username --> Ensure Valid
    # ... Password --> Ensure Valid
    # ... Ensure Username is Not Taken
    # ... Return to Main Menu if Working Properly
    if command == "R":
        
        print("Register for an account")
        user = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")

        valid_u = valid_username(user)
        valid_p = valid_password(password)
        u_exists = username_exists(user)
        

        if valid_u == False:
            print("Username is Invalid, Registration Cancelled!")
            print()
            
        elif valid_p == False:
            print("Password is Invalid, Registration Cancelled!")
            print()

        elif u_exists:
            print("Duplicate username, Registration Cancelled!")
            print()

        # ELSE, the User is Valid & Does NOT Exists
        # ... Password is Valid, Too!
        else:
            add_user(user,password)
            print("Registration Successful!")
            print()

    # ELIF "command" == "L"
    # ... Prompt User For:
    # ... Username & Password --> IF G, Nest WHILE Loop
    # ... Prompt User to Either: Read, Send, Delete Messages, or Logout
    elif command == "L":

        print("Log In")
        user = input("Username (case sensitive): ")
        password = input("Password (case sensitive): ")

        command_string = "L"

        valid_up = check_password(user,password)

        if valid_up:
            print(f"You have been logged in successfully as {user}")
            print()


            while True:
                l_command = str.upper(input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: "))

                while l_command not in "RSDL":
                    print("Invalid Command, Try Again!")
                    print()
                    l_command = str.upper(input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout: "))

                # IF "l_command" == "R", Read All Messages
                # ... Print Messages to the Screen! ("print_messages")
                if l_command == "R":
                    print()
                    
                    if command_string[-1] == "D":
                        print("No messages in your inbox")
                        print()
                        
                    else:
                        print_messages(user)

                        decrypt_prompt = str.upper(input("Would you like to decode one of your messages? (y)es or (n)o: "))

                        while decrypt_prompt not in "YN":
                            print("Invalid Command, Try Again")
                            print()
                            decrypt_prompt = str.upper(input("Would you like to decode one of your messages? (y)es or (n)o: "))

                        if decrypt_prompt == "N":
                            print()

                        else:
                            decode_num = int(input("Which message number would you like to decode? "))

                            while str(decode_num).isnumeric() == False:
                                print("Invalid Command")
                                print()

                            message_num = print_messages_count(user)

                            if decode_num <= message_num:
                                decrypt = str.upper(input("Enter your decryption key (valid commands include 'AXFUDLR'): "))
                                print()
                                for i in range(len(decrypt)):
                                    if decrypt[i] not in "AXFUDLR":
                                        print("Invalid Command")
                                        print()
                                        decrypt = str.upper(input("Enter your decryption key (valid commands include 'AXFUDLR'): "))


                    
                                decrypt_message = decode_message(user,decode_num,decrypt)
                                print(f"Decrypted message: {decrypt_message}")
                                print()

                    command_string += l_command

                # ELIF "l_command" == "D", Delete All Messages
                # ... Delete ALL Messages in "{user}.txt" File ("delete_messages")
                elif l_command == "D":
                    print("Your messages have been deleted")
                    print()
                    delete_messages(user)

                    command_string += l_command

                # ELIF "l_command" == "S", Send Message to Other User
                # ... Prompt User for Receipient & Message
                # ... Ensure Username Receipient Exists
                elif l_command == "S":
                    recepient = input("Username of recipient: ")
                    

                    valid_r = username_exists(recepient)

                    

                    if valid_r == False:
                        print("Unknown recipient")
                        print()

                    else:
                        message = input("Type your message: ")
                        print()
                        
                        encrypt = str.upper(input("Would you like to encrypt your message? (y)es or (n)o: "))
                        while encrypt not in "YN":
                            print("Invalid Command")
                            print()
                            encrypt = str.upper(input("Would you like to encrypt your message? (y)es or (n)o: "))

                        if encrypt == "N":   
                            send_message(user,recepient,message)
                            print("Message sent!")

                        else:
                            encrypt_key = str.upper(input("Enter your encryption key (valid commands include 'AXFUDLR'): "))

                            for i in range(len(encrypt_key)):
                                if encrypt_key[i] not in "AXFUDLR":
                                    print("Invalid Command")
                                    print()
                                    encrypt_key = str.upper(input("Enter your encryption key (valid commands include 'AXFUDLR'): "))

                            new_word = message
                            for c in encrypt_key:

                                # If User Inputted "A" --> Call "add_letters"
                                if c == "A":
                                        
                                    current_word = add_letters(new_word,1)

                                    new_word = current_word


                                elif c == "X":

                                    current_word = delete_characters(new_word,1)
                                    new_word = current_word
                                    
                                elif c == "F":
                                    current_word = flip(new_word)
                                    new_word = current_word

                                elif c == "U":
                                    current_word = ascii_shift(new_word,1)
                                    new_word = current_word
                                    
                                elif c == "D":
                                    current_word = ascii_shift(new_word,-1)
                                    new_word = current_word
                              
                                elif c == "L":
                                    current_word = shift_left(new_word)
                                    new_word = current_word
                                    
                                elif c == "R":
                                    current_word = shift_right(new_word)
                                    new_word = current_word


                            send_message(user,recepient,new_word)
                            print("Message sent!")
                            

                                
                                
                        print()

                    command_string += l_command

                # ELSE "l_command" == "L", Log Out of Username
                # ... Return User to Main Menu --> "break"
                else:
                    print(f"Logging out as username {user}")
                    print()
                    break
                
            


            
        else:
            print("Your Username / Password Combination Does NOT Exist on File")
            print("Please Register Prior to Logging In!")
            print()
        
        


    # ELSE "command" == "Q"
    # ... QUIT System --> "break"
    else:
        print("Goodbye!")
        break


                       
    





    
    
