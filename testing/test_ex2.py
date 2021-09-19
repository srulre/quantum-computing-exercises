import pytest
import ex2
from qiskit import Aer
import numpy as np


def test_bell():
    # Build the first bell state
    ghz_bell = ex2.ghz_generator(2)
    # Run the quantum circuit on a statevector simulator backend
    backend = Aer.get_backend('statevector_simulator')
    bell_state = backend.run(ghz_bell).result().get_statevector(ghz_bell)
    # Compare with expected result from first bell state
    assert np.array_equal(np.round(bell_state, 3), np.round(1 / np.sqrt(2) * np.array([1, 0, 0, 1]), 3))


def test_ghz_error():
    with pytest.raises(ValueError) as e:
        ghz_error = ex2.ghz_generator(-1)
