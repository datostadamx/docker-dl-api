import numpy as np


class perceptron():
    def __init__(self, inputs : list, weights : list, name : str):
        """Generic perceptron object.

        Parameters
        ----------
        inputs : list
            List containing inputs. Will be transformed into a np.array.
        weights : list
            List containing weights. Will be transformed into a np.array.
        name : str, optional
            Name of the perceptron.
        """
        
        assert (len(inputs) != len(weights)), "Lists must have the same size!"

        self.size = len(inputs)
        self.inputs = np.array(inputs)
        self.weights = np.array(weights)
        self.name = name or 'Generic perceptron.'

    def decide(self, bias : int) -> bool:
        """Computes perceptron's output.
        
        Parameters
        ----------
        bias : int
            Integer determining the threshold for the linear map.
        """
        return (self.inputs @ self.weights) >= bias


if __name__ == '__main__':
    inputs = [1, 1, 0, 1]
    weights = [-7, 3, 11, 2]

    p = perceptron(inputs, weights)
    print(p.decide(4))
