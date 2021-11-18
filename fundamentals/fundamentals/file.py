num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # vaarianle declararion, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declation, dictionaty
fruit = ('blueberry', 'strawberry', 'banana') # varainle declration, tuple
print(type(fruit))# log
print(pizza_toppings[1]) # access value
pizza_toppings.append('Mushrooms') # list , add value
print(person['name']) #access value
person['name'] = 'George' # dictionary, change value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2])# tuple, access value

if num1 > 45: # conditional if
    print("It's greater") # log
else: #condtional else
    print("It's lower") # log

if len(string) < 5: # conditional if
    print("It's a short word!") # log
elif len(string) > 15: #condtional else if
    print("It's a long word!") # log
else: #condtional else
    print("Just right!") # log

for x in range(5): # for loop
    print(x) # log
for x in range(2,5): # for loop
    print(x) # log
for x in range(2,10,3): # for loop
    print(x) # log
x = 0
while(x < 5):# while loop
    print(x) # log
    x += 1

pizza_toppings.pop() # delete value
pizza_toppings.pop(1) #delte value

print(person) # log
person.pop('eye_color') #delte value
print(person)# log

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional if
        continue # continue
    print('After 1st if statement') # log
    if topping == 'Olives': #condotional if
        break # break

def print_hello_ten_times(): # log
    for num in range(10): # for loop
        print('Hello') # log

print_hello_ten_times()# log

def print_hello_x_times(x): #log
    for num in range(x): #conditional
        print('Hello') #log

print_hello_x_times(4) #log

def print_hello_x_or_ten_times(x = 10): # log
    for num in range(x): #for loop
        print('Hello') #log

print_hello_x_or_ten_times() # log 
print_hello_x_or_ten_times(4) #log


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)