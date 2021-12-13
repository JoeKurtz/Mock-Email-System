# Mock-Email-System
 A System to Send, Receive, Read, and Encrypt/Decrypt Emails between Users

## Functions
To create the mock email system, I first had to create functions that would perform essential tasks throughout the rest of the code.
These Functions Include:

### Email Setup Functions:
- (1) _valid_username_ : Determines if the username supplied is valid
- (2) _valid_password_ : Determines if the password supplied is valid
- (3) _username_exists_ : Determines if the username already exists in the file 'user_info.txt'
- (4) _check_password_ : Determines if the username / password combination supplied matches one of the user accounts represented in the 'user_info.txt' file
- (5) _add_user_ : If the user being supplied is not already in the 'user_info.txt' file they should be added, along with their password.

### Email Processes Functions:
- (6) _send_message_ : Writes a new line into the specific messages file for the given users with the following information: sender|date_and_time|message\n
- (7) _print_messages_ : Prints all messages sent to the username in question
- (8) _delete_messages_ : Erases all data in the messages file for this user

### Encryption Functions: 
- (9) _ascii_shift_
- (10) _shift_right_
- (11) _shift_left_
- (12) _flip_
- (13) _add_letters_
- (14) _delete_characters_
- (15) _decode_message_

## Email System (w/ Code Examples)
Once ran, the system presents the user with **Three** Options:
1. *Login*
2. *Register*
3. *Quit*

*NOTE*: Basic Data Validation Ensues to Ensure User Complies With Request
```python
command = str.upper(input("(l)ogin, (r)egister or (q)uit: "))
while command not in "LRQ":
  print("Invalid Command, Try Again!")
  print()
  command = str.upper(input("(l)ogin, (r)egister or (q)uit: "))
```

### Register
The User is Prompted to Enter a Username & Password

```python
user = input("Username (case sensitive): ")
password = input("Password (case sensitive): ")
```

The entered Username and Password are passed through the validation functins ouitlined above to ensure the username and password comply with the necessary requirements.
- If the Username exists or doesn't comply with requirements, the user is taken back to the main menu
- If the Password does not comply with requirements, the user is taken back to the main menu

Otherwise, the username and password complies, and the username/password pair is added to the "user_info.txt" file using the "add_user" function <br />
<br />
The Username is also automatically sent a message from the admin to their inbox, timestamped at the current time at registration. For instance, a user that registers at 2:58:04 PM on 12/12/2021 is automatically sent the following message from "admin":

```
admin|12/12/2021 14:58:4|Welcome to your account!
```
<br />
Upon successful registration, the user is returned to the main menu

### Login
Once the user is registered, he is able to successfuly login. The user is prompted to enter in his _username_ and _password_. Given that the user enters the correct username/password pair, he is prompted a list of options of functionality:
1. Read Messages
2. Send a Message
3. Delete all Messages
4. Log Out


#### Read Messages
The User's inbox stored in the messages folder under "{user_name}.txt" is printed onto the screen in Message # \n Timestamp \n Message Format <br />
For instance, user "Abc123" Inbox would print as follows:
```
Message #1 received from admin
Time: 12/12/2021 15:0:22
Welcome to your account!

Message #2 received from Def456
Time: 12/12/2021 15:0:22
Hi, How are you doing?!
```
The user is also asked if they want to decode one of their messages if they have a coded message <br />
For instance, assume user "Abc123" Inbox was follows:
```
Message #1 received from admin
Time: 12/12/2021 15:0:22
Welcome to your account!

Message #2 received from Def456
Time: 12/12/2021 15:0:22
Hi, How are you doing?!

Message #3 received from Def456
Time: 12/12/2021 15:0:22
DSSOH
```
Then, the user is asked:
```
Would you like to decode one of your messages? (y)es or (n)o: _y_
Which message number would you like to decode? _3_
Enter your decryption key (valid commands include 'AXFUDLR'): _DDD_
```
The following would be returned to the request to decode the _third_ message:
```
Decrypted message: APPLE
```

The user is then reprompted which option of functionality they want to perform

#### Send a Message
#### Delete all Messages
The "delete_messages" function is opened up, which opens the user's "{user_name}.txt" file, and all content in the file is deleted, including the message from admin. <br/>
<br/>
If the user then selects read messages, no messages are printed.
#### Log Out
The user is returned to the main menu, where they can once again:
- Log In
- Register
- Quit

### Quit
The system is ended. All data is stored within .txt files for rerun.
