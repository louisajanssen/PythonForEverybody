x = 5
print (x)

x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

n = 5
while n > 0:
    print(n)
    n = n-1
print('Blastoff!')
#Loops have iteration variables that change each time through a loop

#== equal to -> = assignment
#!= not equal

# program to prompt for a score between 0.0 and 1.0. Print error if score out of range.
score = input("Enter Score: ")
s =  float(score)
x = 'Error'
if s >= 0.9:
	x = 'A'
elif s >=0.8:
	x='B'
elif s >=0.7:
	x='C'
elif s >= 0.6:
	x='D'
elif s < .6:
	x ='F'
else:
	x ="Out of Range"
print (x)

# Functions
def thing():
	print('Hello')
	print('Fun')

thing()
print('Zip')
thing()
# We call these reuasable pieces of code functions
# You can use int() and float() to convert between strings and integers

x = 5
print('Hello')

def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day'.)

print('Yo')
print_lyrics() #invoke the function
x = x + 2
print(x)

# Return value
def greet():
	return "Hello"

print(greet()), "Glenn")
print(greet()), "Sally")

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
def computepay(h,r):
    if (h <= 40):
    	pay = h*r
    elif h > 40 :
    	pay = 40 * r + (h-40) * r * 1.5
    return pay 

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)

# Break stataement
while True:
	line = input('> ')
	if line == 'done' :
		break 
	print(line)
print('Done!')