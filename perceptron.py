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

        self.size = None
        self.inputs = None
        self.weights = None
        self.name = None

    def decide(self, bias : int) -> bool:
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
        return None


if __name__ == '__main__':
    pass
