import numpy as np
import qiskit as qk
from qiskit.visualization import plot_histogram
from qiskit import (IBMQ,
                    QuantumCircuit,
                    execute,
                    Aer)

IBMQ.save_account(
    '7dfa239b011c18077028ab2d16443af81fa70064970c97355fe714c5ed49bed81440e839333604176db184479e00dc72d587fe298408fd24bfc08b5d5a8d0d44')

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [0, 1])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)

# Draw the circuit
circuit.draw()
