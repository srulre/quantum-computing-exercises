import pathlib

import pytest
import ex2
from qiskit.quantum_info import Statevector
import numpy as np
import functools


@pytest.mark.parametrize("n_qubits",
                         [1, 2, 6,
                          pytest.param(0, marks=pytest.mark.xfail(raises=ValueError)),
                          pytest.param(-1, marks=pytest.mark.xfail(raises=ValueError))])
def test_ghz(n_qubits):
    n_qubits = ex2.GHZConfigModel(qubit_count=n_qubits).qubit_count
    ghz_bell = ex2.ghz_generator(n_qubits)
    # Evolve the 0 ... 0 state on the circuit
    state = Statevector.from_int(0, 2 ** n_qubits)
    state = state.evolve(ghz_bell)
    result = state.data
    # Compare with expected result
    expected_result = np.zeros(2 ** n_qubits)
    expected_result[0] = 1
    expected_result[-1] = 1
    expected_result = expected_result / np.sqrt(2)

    assert np.allclose(result, expected_result)


@pytest.mark.parametrize("relative_output_path",
                         ["",
                          "output_test.png",
                          "test_output_1",
                          "test_output_2/output_test.png"])
def test_output_path_draw(relative_output_path, tmp_path):
    output_path = tmp_path / relative_output_path
    ghz_model = ex2.GHZConfigModel(output_path=str(output_path))

    ghz_state_circuit = ex2.ghz_generator(ghz_model.qubit_count)
    ghz_state_circuit.draw(output='mpl',
                           filename=ghz_model.output_path)
    assert pathlib.Path(ghz_model.output_path).exists()
