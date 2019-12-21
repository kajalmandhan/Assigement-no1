#Q:01
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
#Q:02
import sys
print("Python Version")
print(sys.version)
print("Version Info")
print(sys.version_info)
#Q:03
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
#Q:04
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str() + " is: " + str(pi * r**2))
#Q:05
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
#Q:06
num1 = input()
num2 = input()

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))