'''price = 10
price = 20
print(price)
name = 'shamim'
is_published = True
# input 
name = input('what is your name? ')
print("hi "+ name)
fav_color = input('what is your fav color?')
print (name +' likes '+ fav_color)
# type conversion
birth_year = input('birth year: ')
print(type(birth_year))
age = 2024-int(birth_year)
print(age)

weight_lbs = input('weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)'''

'''# Strings
course = "python's for beginers"
mult_line = ''''''hi jdasndn
ncdcn
cdsncion
dcnodnc'''
'''print(course)
print(course[-2])
print(course[0:5])
print(mult_line)

#formatted string
first = 'shamim'
last = 'khan'
message = first + '[' + last + ']' + 'is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)
print(message)

#string methodes
name = 'shamim ali'
print(len(name))
print(name.upper())
print(name.find('s'))
print(name.replace('ali', 'khan'))

#math operator
import math
print(math.ceil(2.9))
print(math.floor(2.9))'''

#if statement
is_hot = False
is_cold = False
if is_hot:
    print('it is a hot day')
elif is_cold:
    print('it is a cold day')
else:
    print('it is a nice day')
print('enjoy your day')