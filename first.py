######First AI program
print("NUERL PROGRAM")
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
######Start
training_input=np.array([[0,0,1],[1,1,1],[1,0,0],[0,1,1]] )
training_output=np.array([0,1,1,0] ).T
np.random.seed(1)
synaptic_weights=2*np.random.random((3,1))-1
print("Random weigts:")
print(synaptic_weights)
for iteration in range (1):
    input_layer=training_input;
    output=sigmoid(np.dot(input_layer,synaptic_weights))
#num1=int(input("Enter the first number:"))
#print("outofsig:", sigmoid(num1))
print("output after training:")
print(output)