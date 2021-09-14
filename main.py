import numpy as np
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

    ### Ex 1
    # create the circuit object for the bell state generator
    bell_state_circuit = bell_generator()
    # draw in console
    print(bell_state_circuit)
    # draw in graph
    bell_state_circuit.draw('mpl')

    ### Ex 2
    # create the circuit object for the bell state generator
    ghz_state_circuit = ghz_generator(5)
    # draw in console
    print(ghz_state_circuit)
    # draw in graph
    ghz_state_circuit.draw('mpl')


