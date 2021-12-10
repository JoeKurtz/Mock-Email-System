# Mock-Email-System
 A System to Send, Receive, Read, and Encrypt/Decrypt Emails between Users

## Functions
To create the mock email system, I first had to create functions that would perform essential tasks throughout the rest of the code.
These Functions Include:

### Email Setup Functions:
(1) valid_username : Determines if the username supplied is valid
(2) valid_password : Determines if the password supplied is valid
(3) username_exists : Determines if the username already exists in the file 'user_info.txt'
(4) check_password : Determines if the username / password combination supplied matches one of the user accounts represented in the 'user_info.txt' file
(5) add_user : If the user being supplied is not already in the 'user_info.txt' file they should be added, along with their password.

### Email Processes Functions:
(6) send_message
(7) print_messages
(8) delete_messages
(15) decode_message

### Encryption Functions: 
(9) ascii_shift
(10) shift_right
(11) shift_left
(12) flip
(13) add_letters
(14) delete_characters
'''
