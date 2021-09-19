import numpy as np
import argparse
import pathlib
from pydantic import BaseModel, ValidationError
from typing import Optional
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram


class GHZConfigModel(BaseModel):
    qubit_count: int
    output_path: Optional[str] = None


def ghz_generator(n_qubits: int) -> QuantumCircuit:
    if n_qubits < 1:
        raise ValueError("Qubit count must be larger than 0")
    # Create a Quantum Circuit with n qubits
    circuit = QuantumCircuit(n_qubits)
    # Add a H gate on qubit 0
    circuit.h(0)
    for qubit in range(1, n_qubits):
        # Add a CX (CNOT) gate on corresponding control qubit and target qubit
        circuit.cx(0, qubit)

    return circuit


if __name__ == '__main__':

    ### Ex 2.1
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--config_path", type=str,
                        help="JSON configuration path")
    args = parser.parse_args()

    # parse to pydantic
    try:
        ghz_config = GHZConfigModel.parse_file(args.config_path)
    except ValidationError as e:
        print(e)
        raise e

    # extract qubit count
    n_qubits = ghz_config.dict()["qubit_count"]

    # process output path
    output_path_str = ghz_config.dict()["output_path"]
    if not output_path_str:
        output_path = pathlib.Path.cwd() / 'output.png'  # default output path is the current working directory
    else:
        output_path = pathlib.Path(output_path_str)

    # create the circuit object for the bell state generator
    ghz_state_circuit = ghz_generator(n_qubits)
    # draw in graph
    ghz_state_circuit.draw(output='mpl',
                           filename=str(output_path))
