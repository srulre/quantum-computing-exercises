import pathlib

import pytest
import ex2
from qiskit.quantum_info import Statevector
import numpy as np
import functools


@pytest.mark.parametrize("n_qubits", [1, 2, 6])
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

    assert np.array_equal(np.round(result, 3), np.round(expected_result, 3))

def test_ghz_error():
    with pytest.raises(ValueError) as e:
        ghz_error = ex2.GHZConfigModel(qubit_count=-1).qubit_count

@pytest.mark.parametrize("output_path_name",
                         ["",
                          "/Users/israelreichental/downloads",
                          "/Users/israelreichental/downloads/output_test.png",
                          "/Users/israelreichental/downloads/test_output_1",
                          "/Users/israelreichental/downloads/test_output_2/output_test.png"])
def test_output_path_empty(output_path_name):
    ghz_model = ex2.GHZConfigModel(output_path=output_path_name)
    output_path = pathlib.Path(ghz_model.output_path)

    ghz_state_circuit = ex2.ghz_generator(ghz_model.qubit_count)
    ghz_state_circuit.draw(output='mpl',
                           filename=str(output_path))
    pathexists = output_path.exists()
    # remove leftover file
    if pathexists:
        output_path.unlink()
        # remove leftover folders
        for leftover_dir in ["test_output_1", "test_output_2"]:
            if leftover_dir in str(output_path):
                output_path.parents[0].rmdir()
                break
    assert pathexists

