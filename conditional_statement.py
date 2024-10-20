light = input ('light is :-')
if(light == "red"):
    print('stop')
elif(light == "green"):
    print('go')
elif(light == "yellow"):
    print('slow')
else:
    print('light is broken')

food = input ('food: ')
print('yes') if(food == "cake") else print('no')

age = int(input('age: '))
vote = ('yes','no')[age<18]
print(vote)  # prints 'no' if age is less than 18, 'yes'