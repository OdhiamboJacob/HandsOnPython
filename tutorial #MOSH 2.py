import math
# string methods
'''
 len() # number of characters in the string
 course.upper()
 course.lower()
 courae.find()
 course.replace()
 '....' in course
'''
# arithmetic operations
'''
 int
 float
'''
# math functions
'''
x = 2.9
print(round(x))
# If Statements
is_hot = False
is_cold =False
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print('wear warm clothes')
else:
    print('Good day')
print((10/100)*1000000)
print((20/100)*1000000)
# Exe
price = 1000000
good = 10/100
bad = 20/100
'''
'''
buyer = input('key in buyer')
if buyer == 'good':
    print(good*price)
elif buyer == 'bad':
    print(bad*price)
'''
# Logical operators
# used for multiple conditions
'''
and - when both conditions are true
or - when one of the conditions is true
not - when changing the bool to otherwise
'''
'''
goodcredit = False
criminal = False
if goodcredit or criminal:
    print('give loan')
else:
    print('no loan')
'''
# comparison operators
'''
greater than - >
less than - <
equal to - ==
not equal - !=
less than or equal to - <=
greater than or equal to - >=
'''
# Exe
'''
name = 'fhdrgfc'
if len(name) >= 3 and len(name) <= 50:
    print('name looks good')
elif len(name) < 3:
    print('name must be at least three characters')
elif len(name) >= 50:
    print('name must be a maximum of 50 characters')
else:
    print('fuck off')
'''
# weight converter
'''
weight = int(input( 'weight: '))
L = 2.222
K = 0.45
unit = eval(input('lbs or kg: '))
if unit == L:
    print(weight*L)
if unit == K:
    print(weight*K)
'''
# While loops
''''
used to execute a block of code multiple times eg programmes and games.
syntax - while , condition: then codes bellow
'''
'''
i = 1
while i <= 5:
    print('1' * i) # this line alone will end up in an infinite loop coz one will remain one and less than 5 forever.
    i = i + 1
print('Done')
'''
# guessing game
'''
secret = 9
guess_count = 0
gues_limit = 3
while guess_count < gues_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret:
        print('you won')
        break
else:
    print('sorry you faild')
'''
'''
# car game
comand = ''
started = False
while True:
    comand = input('>').lower()
    if comand == 'start':
        if started:
            print('Hell..! car is already started,,!')
        else:
            started = True
            print('Great,,! car has started...')
    elif comand == 'stop':
        if not started:
            print('crout..! car is already stopped')
        else:
            started = False
            print('wow..! car has stopped..')
    elif comand == 'help':
        print(''
        start - to start the car
        stop - to stop the car
        quit - to quit
        '')
    elif comand == 'quit':
        break
    else:
        print('sorry i do not understand you')
'''
'''
# for Loops
# for item in range(0,30,2):
#     print(item)
# exe
prices = [10,25,32,36,354,32,28]
sum = 0
for item in prices:
    sum = sum + item
print(f'Total:', sum)
'''
'''
# Nested loop
# for x in range (10):
#     for y in range(3):
#        print(f'({x},{y})')
# Exe
numbers = [2,2,2,2,2,10]
# for items in numbers:
#     print('x'* items)
 for items in numbers:
    output = ''
    for count in range(items):
        output = output + 'x'
    print(output)
# shape trial
triangle = [1,2,3,4,5,6,7,8,9,]
for dogs in triangle:
    result = ''
    for ideas in range(dogs):
        result = result + 'A'
    print(result)
'''
'''
# Lists
# names = ['jowi','kalu','goli','tyu']
# names[1] = 'kilo'
# print(names[:])
numbers = [1,2,3,4,5,6,18,7,9,8,5]
max = numbers[0]
for item in numbers:
    if item > max:
        max = item
print(max)
'''
'''
# 2D lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][2] = 13
print(matrix[0][2])
for row in matrix:
    for item in row:
        print(item)
        
# List Methods
numbers = [3,4,5,6,3,5,6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#Tuples
numbers = (1,2,3)
print(numbers[1])

#unparking
coordinates = [1,2,3]
x,y,z = coordinates
print(y)

#dictionaries
phone = input("phone: ")
digit_def = {
    "1": "one",
    "2": "two",
    "3": "three"
    }
output = " "
for ch in phone:
    output += digit_def.get(ch, " ! ")+ " "
print(output)

#emoji converter
messege = input(">")
words = messege.split(' ')
emojis = {
    ":)": "😊" ,
    ":(": "😞"
}
output = " "
for word in words:
    output += emojis.get(word, word) +" "
print(output)

#functions
def greet_user():
    print('Hi there')
    print('welcome aboard')


print("start")
greet_user()
print("Finish")


#Parameter
def greet_user(fast_name, last_name):
    print(f'Hi {fast_name} {last_name}!')
    print('welcome aboard')


print("start")
greet_user("John","Jowii")
greet_user("Mary", "Gucii")
print("Finish")

#keyword arguments
#first_name = "jak", last_name ="jowii"

#return statement.
def square(number):
    return number * number

square(3)
name = input()
result = square(2)
print(result)
print(name)

#Exception
try:
    age = int(input('age: '))
    income = 2000
    risk = income/age
    print (age)
    print(risk)
except ZeroDivisionError:
    print('age cannot be zero:')
except ValueError:
    print('invalid value')

#comments
print('# precides comments')

# classes
# used to define new types and real concepts
class Point:
    def __init__(self,x,y): //constructor
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

Point1 = Point( 10,20)
Point1.x = 10
Point1.y = 20
print(Point1.x)
Point1.draw()

point2 = Point(23,56)
point2.x =24
print(point2.x)
# constractor = function called at the time of creating an object.


#EXE
class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi I am {self.name}')


jack = Person('jack jowii')

jack.talk()
'''

# inheritance
#2.59.10
def studentsPerformnce():
    n=eval(input('enter the number of students;'))
    detils=[]
    for i in range(n):
        name = input('Enter the name of student')
        english = int(input('English ; '))
        kiswahili =int(input('Kiswahili ; '))
        sum= english+kiswahili
        myDit={
            name:{
                'Kiswahili':kiswahili,
                'English':english,
                "Sum":sum
            }
        }
        detils.append(myDit)
    print(detils)
studentsPerformnce()







