######Calculator program
def add(x, y):

    return x + y

######Start
print("CALCULATOR PROGRAM")
print("select operation")
print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")
print("5.SQR")
choice=input("Enter choice (1/2/3/4/5):")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if choice =='1':
  print(num1, "+", num2, "=", add(num1,num2))
    
    #else
    #print("invalid")