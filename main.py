import numpy as np
import argparse
import pathlib
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram


def bell_generator() -> QuantumCircuit:
    # Create a Quantum Circuit with 2 qubits
    circuit = QuantumCircuit(2)
    # Add a H gate on qubit 0
    circuit.h(0)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
    circuit.cx(0, 1)

    return circuit


def ghz_generator(n_qubits: int) -> QuantumCircuit:
    # Create a Quantum Circuit with n qubits
    circuit = QuantumCircuit(n_qubits)
    # Add a H gate on qubit 0
    circuit.h(0)
    for qubit in range(1, n_qubits):
        # Add a CX (CNOT) gate on corresponding control qubit and target qubit
        circuit.cx(0, qubit)

    return circuit


if __name__ == '__main__':
    print("Hello World")

    ### Ex 1.1
    # create the circuit object for the ghz state generator
    bell_state_circuit = bell_generator()
    # draw in console
    print(bell_state_circuit)
    # draw in graph
    bell_state_circuit.draw('mpl')

    ### Ex 1.2
    # create the circuit object for the ghz state generator
    ghz_ex2_state_circuit = ghz_generator(5)
    # draw in console
    print(ghz_ex2_state_circuit)
    # draw in graph
    ghz_ex2_state_circuit.draw('mpl')

    ### Ex 1.3
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--qubit_count", type=int,
                        help="number of qubits")
    parser.add_argument("-o", "--output_path", type=str,
                        help="output path for circuit. If none, use current working directory")
    args = parser.parse_args()

    # process qubit count
    n_qubits = args.qubit_count
    if not n_qubits:
        n_qubits = 2  # default ghz state will be the first bell state
    if n_qubits < 2:
        raise ValueError("Qubit count must be larger than 1")

    # process output path
    output_path_str = args.output_path
    if not output_path_str:
        output_path = pathlib.Path.cwd()  # default output path is the current working directory
    else:
        output_path = pathlib.Path(output_path_str)
    # create output folder if doesn't exist yet
    if not output_path.exists():
        output_path.mkdir()

    # create the circuit object for the bell state generator
    ghz_state_circuit = ghz_generator(n_qubits)
    # draw in graph
    ghz_state_circuit.draw(output='mpl', filename=pathlib.Path(output_path, 'output.png'))