import argparse
import pathlib
import pydantic
from typing import Optional
from qiskit import QuantumCircuit


class GHZConfigModel(pydantic.BaseModel):
    qubit_count: pydantic.PositiveInt = 2
    output_path: str = pathlib.Path.cwd() / 'output.png'

    @pydantic.validator('output_path')
    def output_path_exists(cls, v):
        v_path = pathlib.Path(v)
        v_path_dir = v_path if not v_path.suffix else v_path.parents[0]
        if not v_path_dir.exists():  # create folder
            v_path_dir.mkdir(parents=True)
        if not v_path.suffix:
            v_path = v_path / 'output.png'
        return v_path


def ghz_generator(n_qubits: int) -> QuantumCircuit:
    circuit = QuantumCircuit(n_qubits)
    circuit.h(0)
    for qubit in range(1, n_qubits):
        circuit.cx(0, qubit)

    return circuit


if __name__ == '__main__':
    ### Ex 2.1
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--config_path", type=str,
                        help="JSON configuration path")
    args = parser.parse_args()

    # parse to pydantic and process input
    ghz_config = GHZConfigModel.parse_file(args.config_path)
    n_qubits = ghz_config.qubit_count
    output_path = ghz_config.output_path

    ghz_state_circuit = ghz_generator(n_qubits)
    ghz_state_circuit.draw(output='mpl',
                           filename=str(output_path))
