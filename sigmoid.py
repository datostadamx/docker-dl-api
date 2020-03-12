import numpy as np


class sigmoid_neuron():
    def __init__(self, n : int):
        """Constructor method.

        Parameters
        ----------
        n : int
            The number of synaptic connections, a vector.
        """

        np.random.seed(123) # We set a random seed for reproductibility
        self.synaptic_weights = 2 * np.random.random((n, 1)) - 1

    def __sigmoid(self, x : np.ndarray) -> np.ndarray:
        """Sigmoid function.
        
        Parameters
        ----------
        x : numpy.ndarray
            The vector to be evaluated on the standard sigmoid function.

        Returns
        -------
        s : np.ndarray
            The standard sigmoid function evaluated on the input vector.
        """

        s = 1 / (1 + np.exp(-x))
        return s

    def __sigmoid_derivative(self, x : np.array) -> np.array:
        """The derivative of the evaluated sigmoid function.
        
        Parameters
        ----------
        x : numpy.ndarray
            The sigmoid evaluated vector to be evaluated on its derivative.

        Returns
        -------
        s : np.ndarray
            The sigmoid derivative evaluated vector.
        """

        s = x * (1 - x)
        return s

    def train(self, tr_inputs : np.array, tr_outputs : np.array, iters : int):
        """Training method. Updates the synaptic weights of the neuron.
        
        Parameters
        ----------
        tr_inputs : numpy.ndarray
            The vector with features for training.
        tr_outputs : numpy.ndarray
            The vector with labels for training.
        iters : int, optional
            The number of epochs for training.
        """

        for iteration in range(iters):
            output = self.predict(tr_inputs)
            error = tr_outputs.reshape((len(tr_inputs), 1)) - output
            adjustment = np.dot(tr_inputs.T, error *
                                self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def predict(self, inputs : np.array) -> np.array:
        """Sigmoid function.
        
        Parameters
        ----------
        inputs : numpy.ndarray
            The input vector from which the prediction is made.

        Returns
        -------
        p : np.ndarray
            A prediciton vector.
        """

        p = self.__sigmoid(np.dot(inputs, self.synaptic_weights))
        return p


if __name__ == '__main__':
    # Initialize sigmoid neuron
    sigmoid = sigmoid_neuron(2)
    print("Initial weights (random):")
    print(sigmoid.synaptic_weights)

    # Training data
    training_inputs = np.array([(1, 0), (0, 0), (0, 1)])
    training_output = np.array([1, 0, 1]).T.reshape((3, 1))

    # Neuron training
    sigmoid.train(training_inputs, training_output, 10)
    print("Final synaptic weights (after training): ")
    print(sigmoid.synaptic_weights)

    # Predict for unseen data
    print("Prediction for (1, 1): ")
    print(sigmoid.predict(np.array((1, 1))))
