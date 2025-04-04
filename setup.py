from setuptools import setup, find_packages

setup(
    name="neurospark",
    version="0.1.0",
    author="Your Name",
    description="Advanced 3D neuron morphology visualization and sampling toolkit",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pyvista",
        "networkx"
    ],
    python_requires=">=3.7",
)
