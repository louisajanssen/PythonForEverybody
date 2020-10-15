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

#Functions
def thing():
	print('Hello')
	print('Fun')

thing()
print('Zip')
thing()
#We call these reuasable pieces of code functions