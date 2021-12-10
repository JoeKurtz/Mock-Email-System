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
Once ran, the system present the user with **Three** Options:
1. *Login*
2. *Register*
3. *Quit*

*NOTE*: Basic Data Validation Ensues to Ensure User Complies With Request
```
command = str.upper(input("(l)ogin, (r)egister or (q)uit: "))
while command not in "LRQ":
  print("Invalid Command, Try Again!")
  print()
  command = str.upper(input("(l)ogin, (r)egister or (q)uit: "))
```
