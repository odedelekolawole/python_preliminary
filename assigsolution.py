# 1) Declare two variable with your first name and last name and assignment to them your first name and last anme simulteneously
# 2) Retrieve the first three letter of the first name
# 3) Retrieve the last three letter of the last name
# 4) Join the two names
# 5) Return the number of character in the combined names
# 6) Display all the character in the name.


first_name  =    'Kolawole'
last_name   =    'Odedele'

first_three = first_name[:3]
print(first_three)

last_three = last_name[-3:]
print(last_three)


join_name = first_name + " " + last_name
print(join_name)

char_num = len(join_name)
print(char_num)

dispaly_all = ''.join(join_name)
print(dispaly_all)

display_all1 = list("".join(join_name))
print(display_all1)