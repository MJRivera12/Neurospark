# Neurospark, created by Michael J. Rivera -- For easier Neuroscience!

**Neurospark** is a Python package for high-level, customizable 3D visualization and sampling of neuron morphologies — going beyond the limitations of NEUROM.

## Features

- Load and parse `.swc` and `.asc` neuron morphology files.
- Uniform, distance-based, and branch-point-focused 3D sampling.
- Interactive PyVista-based 3D visualizations.
- Generate synthetic neurons for quick prototyping.

## Installation

```bash
pip install -e .
```

## Quickstart

```python
from neurospark import load_morphology, sample_neuron, visualize_neuron

data = load_morphology("neuron.swc")
sampled = sample_neuron(data, strategy="distance", resolution=25)
visualize_neuron(sampled)
```

## License

MIT
