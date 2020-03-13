import numpy as np


class perceptron():
    def __init__(self, inputs, weights, name=None):
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

        self.size = len(inputs)
        self.inputs = np.array(inputs)
        self.weights = np.array(weights)
        self.name = name or 'Generic perceptron.'

    def decide(self, bias):
        """Computes perceptron's output.
        
        Parameters
        ----------
        bias : int
            Integer determining the threshold for the linear map.
        
        Returns
        -------
        bool
            The linear decision.
        """
        
        return (self.inputs @ self.weights) >= bias


if __name__ == '__main__':
    inputs = [1, 1, 1, 1, 0]
    weights = [-5, 7, 3, -2, 1]
    datostada = perceptron(inputs, weights)
    prediction = datostada.decide(6)
    print("Veredicto:", prediction)
