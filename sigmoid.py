import numpy as np


class sigmoid_neuron():
    def __init__(self, n, w=None):
        """Constructor method.

        Parameters
        ----------
        n : int
            The number of synaptic connections, a vector.
        """
        
        if w is not None:
            weights = np.loadtxt(w)
            self.synaptic_weights = weights
        else:
            np.random.seed(123) # We set a random seed for reproductibility
            self.synaptic_weights = 2 * np.random.random((n, 1)) - 1
    
    def save_weights(self, filename='algo.txt'):
        np.savetxt(filename, self.synaptic_weights)

    def __sigmoid(self, x):
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

    def __sigmoid_derivative(self, x):
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

        ds = x * (1 - x)
        return ds

    def train(self, tr_inputs, tr_outputs, iters):
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

    def predict(self, inputs):
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
    s = sigmoid_neuron(2)
    print("Pesos aleatorios:")
    print(s.synaptic_weights)

    # Training data
    tr_inputs = np.array([(0, 1), (1, 0), (0, 0)])
    tr_outputs = np.array([1, 1, 0])

    # Neuron training
    print("Iniciamos entrenamiento:")
    s.train(tr_inputs, tr_outputs, 10000)
    print("Pesos entrenados:")
    print(s.synaptic_weights)

    # Predict for unseen data
    print("Predicción:")
    p = s.predict((1, 1))
    print(p)
    
    # Save weights
    s.save_weights()