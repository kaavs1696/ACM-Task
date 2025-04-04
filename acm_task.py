from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2)

qc.h([0, 1])
qc.cz(0, 1)

qc.h([0, 1])
qc.x([0, 1])
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x([0, 1])
qc.h([0, 1])

qc.measure([0, 1], [0, 1])

# Get simulator backend
sim = AerSimulator()

# Transpile and run the circuit
transpiled_qc = transpile(qc, sim)
result = sim.run(transpiled_qc, shots=1024).result()
counts = result.get_counts()

print("Measurement results:", counts)
plot_histogram(counts)
plt.show()