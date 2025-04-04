import numpy as np
from neurospark.sampler import sample_neuron

def test_sample_uniform():
    points = np.array([[0, 0, 0], [1, 1, 1]])
    data = np.hstack((np.zeros((2, 2)), points, np.zeros((2, 2))))
    sampled = sample_neuron(data, strategy='uniform', resolution=10)
    assert sampled.shape[0] == 10
