# here we run the functions for user_input
from bizz_and_zzuu_functions import *

# Call the functions
while True:
    user_input = int(input('Please enter a number:'))

    if user_input == 0:
        break
    if user_input != 0:
        print(user_input)
        print(test(user_input))
print('Thanks for playing')