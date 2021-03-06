
from random import random
from math import exp

class Perceptron:
    
    # constructor
    def __init__(self, size):
        """ This is perceptron, the base component of neural network
            size: amount of inputs
        """
        self.weights = [0.7037622574353122, 0.32062734201986753, -0.5060893642271465, -0.7281457029531304]
        self.bias = 0.08683967162218453 # random()
        # for i in range(size):
        #     self.weights.append(random() * 2 -1)

    def predict(self, inputs):
        output = 0
        for i, w in zip(self.weights, inputs):
            output += i * w

        # Add bias
        output += self.bias

        # Apply activation function
        return self.activate(output)


    def activate(self, num):
        """
        Activation function
        """
        output = 1/(1+ exp(-num)) + exp(num)/(exp(num)+1)
        return output


    
