import argparse
import pathlib
from qiskit import QuantumCircuit


def ghz_generator(n_qubits: int = 2) -> QuantumCircuit:
    circuit = QuantumCircuit(n_qubits)
    circuit.h(0)
    for qubit in range(1, n_qubits):
        circuit.cx(0, qubit)

    return circuit


if __name__ == '__main__':
    print("Hello World")

    ### Ex 1.1
    bell_state_circuit = ghz_generator(n_qubits=2)
    print(bell_state_circuit)
    bell_state_circuit.draw('mpl')

    ### Ex 1.2
    ghz_ex2_state_circuit = ghz_generator(5)
    print(ghz_ex2_state_circuit)
    ghz_ex2_state_circuit.draw('mpl')

    ### Ex 1.3
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--qubit_count", type=int, default=2,  # default ghz state will be the first bell state
                        help="number of qubits")
    parser.add_argument("-o", "--output_path", type=str, default=pathlib.Path.cwd() / 'output.png',
                        help="output path for circuit. If none, use current working directory")
    args = parser.parse_args()

    # process qubit count
    n_qubits = args.qubit_count
    if n_qubits < 1:
        raise ValueError("Qubit count must be larger than 0")

    # process output path
    output_path_str = args.output_path
    output_path = pathlib.Path(output_path_str)
    if not output_path.exists():
        output_path.mkdir(parents=True)

    # create the circuit object for the ghz state generator
    ghz_state_circuit = ghz_generator(n_qubits)
    ghz_state_circuit.draw(output='mpl',
                           filename=str(output_path))
