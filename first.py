######Calculator program
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
def pwr(x, y):
    return pow(x,y)
######Start
print("CALCULATOR PROGRAM")
print("select operation")
print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")
print("5.PWR")
choice=input("Enter choice (1/2/3/4/5):")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if choice =='1':
  print(num1, "+", num2, "=", add(num1,num2))

elif choice =='2':
  print(num1, "-", num2, "=", sub(num1,num2))
elif choice =='3':
  print(num1, "x", num2, "=", mul(num1,num2))
elif choice =='4':
  print(num1, "/", num2, "=", div(num1,num2))
elif choice =='5':
  print(num1, "^", num2, "=", pwr(num1,num2))
    
    #else
    #print("invalid")