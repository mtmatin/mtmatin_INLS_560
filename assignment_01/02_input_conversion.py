# input() is always captured as a string so you have to 
# "cast" i 

'''
num_1 = input("Your first number: ")
num_2 = input("Your second number: ")

print("The sum of your two numbers is", (num_1) + (num_2), '.')
'''

num_1 = float(input("Your first number: "))
num_2 = float(input("Your second number: "))

print(num_1 / num_2)