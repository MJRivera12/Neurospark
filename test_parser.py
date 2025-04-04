from neurospark.parser import _load_swc
import numpy as np

def test_load_swc():
    test_data = "1 1 0.0 0.0 0.0 1.0 -1\n2 3 0.0 1.0 0.0 0.5 1"
    with open("temp.swc", "w") as f:
        f.write(test_data)
    result = _load_swc("temp.swc")
    assert result.shape[0] == 2
