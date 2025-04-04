import numpy as np

def generate_mock_neuron(branches=3, points_per_branch=20, noise=0.1):
    base = np.zeros((1, 3))
    branches_out = []
    for b in range(branches):
        angle = b * (2 * np.pi / branches)
        direction = np.array([np.cos(angle), np.sin(angle), 1.0])
        direction /= np.linalg.norm(direction)
        path = np.cumsum(np.random.normal(direction, noise, (points_per_branch, 3)), axis=0)
        branches_out.append(path)
    return np.vstack([base] + branches_out)
