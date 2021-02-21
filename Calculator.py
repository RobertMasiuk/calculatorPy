# first program
print("this is simple calculator")
'''
fist = int(input("give first number"))
second =  int(input("give socond number"))
print(fist + second)

'''

mathOperation = input("input type of math operation")

fist = int(input("enter first number"))
second =  int(input("enter socond number"))

if mathOperation == '+':
    print(fist + second)
if mathOperation == '-':
    print(fist - second)
if mathOperation == '*':
    print(fist * second)
if mathOperation == '/' and second !=0:
    print(fist / second)
else:
    print("you can't divide by '0'")