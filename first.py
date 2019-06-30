######First AI program
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
######Start
print("NUERAL  PROGRAM")
num1=int(input("Enter the first number:"))
print("outofsig:", sigmoid(num1))
