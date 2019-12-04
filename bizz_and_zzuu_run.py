# here we run the functions for user_input
from bizz_and_zzuu_functions import *

# Call the functions
while True:
    user_input = input('Please enter a number:')
    if user_input == 'done':
        break
    num =int(user_input)
    if num % 3 == 0 and num % 5 == 0:
        print(div_by_3_and_5(num))
    elif num % 3 ==0:
        print(div_by_3(num))
    elif num % 5 == 0:
        print(div_by_5(num))
    elif num % 3 != 0 and num % 5 != 0:
        print(not_div_by_3_or_5(num))
print('Thank you for playing')