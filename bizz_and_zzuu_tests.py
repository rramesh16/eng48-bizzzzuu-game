from bizz_and_zzuu_functions import *

# Tests go here for separation of concern

# Make test for div_by_3

print("Testing div_by_3 with number: 9. Expected --> 'bizz'")
print(div_by_3(9) == 'bizz')
print('got:', div_by_3(9) )

#Make test for div_by_5

print("Testing div_by_5 with number: 20. Expected --> 'zzuu'")
print(div_by_5(20) == 'zzuu')
print('got:', div_by_5(20))


# Make test for div_by_3_and_5

print("Testing div_by_3_and_5 with number: 15. Expected --> 'bizzzzuu'")
print(div_by_3_and_5(15) == 'bizzzzuu')
print("got:", div_by_3_and_5(15))

# Make test for not_div_by_3_or_5

print("Testing not_div_by_3_or_5 with number: 56. Expected --> 'none'")
print(not_div_by_3_or_5(56) == 'none')
print("got:", not_div_by_3_or_5(56))

