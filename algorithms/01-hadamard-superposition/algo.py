import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qlab import counts, out, save_circuit, save_grid


def one_h(start):
    qc = QuantumCircuit(1)
    if start:
        qc.x(0)
    qc.h(0)
    return qc


def two_h(start):
    qc = QuantumCircuit(1)
    if start:
        qc.x(0)
    qc.h(0)
    qc.h(0)
    return qc


def uniform(n):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    return qc


def measured(qc):
    m = qc.copy()
    m.measure_all()
    return m


def save_amps(path):
    fig, axs = plt.subplots(1, 2, figsize=(8, 3.2))
    for ax, s, name in zip(axs, (0, 1), ("H|0> = |+>", "H|1> = |->")):
        amp = Statevector(one_h(s)).data.real
        ax.bar(["|0>", "|1>"], amp, color=["tab:blue" if a > 0 else "tab:red" for a in amp])
        ax.axhline(0, color="k", lw=0.8)
        ax.set_ylim(-1, 1)
        ax.set_title(name + "  (amplitudes)")
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    d = out(__file__)
    for s in (0, 1):
        print(f"H|{s}> amplitudes:", np.round(Statevector(one_h(s)).data, 4))
    print("H.H|0> amplitudes:", np.round(Statevector(two_h(0)).data, 4))
    print("H.H|1> amplitudes:", np.round(Statevector(two_h(1)).data, 4))
    u = Statevector(uniform(3))
    print("H^3|000> amplitudes:", np.round(u.data.real, 4))
    items = [
        ("measure H|0>", counts(measured(one_h(0)))),
        ("measure H|1>", counts(measured(one_h(1)))),
        ("measure H.H|0>", counts(measured(two_h(0)))),
        ("measure H.H|1>", counts(measured(two_h(1)))),
    ]
    for t, c in items:
        print(t, dict(sorted(c.items())))
    save_grid(items, d / "interference_histograms.png")
    save_amps(d / "amplitudes.png")
    save_circuit(two_h(1), d / "circuit.png")
    save_grid([("uniform superposition of 3 qubits", counts(measured(uniform(3))))], d / "uniform3.png", cols=1)


if __name__ == "__main__":
    main()

