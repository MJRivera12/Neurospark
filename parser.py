import numpy as np

def load_morphology(file_path):
    if file_path.endswith('.swc'):
        return _load_swc(file_path)
    elif file_path.endswith('.asc'):
        return _load_asc(file_path)
    else:
        raise ValueError("Unsupported file format. Use .swc or .asc")

def _load_swc(path):
    data = []
    with open(path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = list(map(float, line.strip().split()))
            data.append(parts)
    return np.array(data)

def _load_asc(path):
    coords = []
    with open(path) as f:
        for line in f:
            if '(' in line and ')' in line:
                parts = line.strip().split()
                x, y, z = map(float, parts[1:4])
                coords.append([x, y, z])
    return np.array(coords)
