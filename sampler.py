import numpy as np

def sample_neuron(morph_data, strategy='uniform', resolution=10):
    if morph_data.shape[1] >= 7:
        coords = morph_data[:, 2:5]
    else:
        coords = morph_data

    segments = []
    for i in range(1, len(coords)):
        p1 = coords[i-1]
        p2 = coords[i]
        if strategy == 'uniform':
            seg = np.linspace(p1, p2, resolution)
        elif strategy == 'distance':
            dist = np.linalg.norm(p2 - p1)
            steps = max(int(dist * resolution), 2)
            seg = np.linspace(p1, p2, steps)
        elif strategy == 'branch_point_focus':
            weights = np.geomspace(1, 0.1, resolution).reshape(-1, 1)
            seg = (1 - weights) * p1 + weights * p2
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
        segments.append(seg)
    return np.vstack(segments)
