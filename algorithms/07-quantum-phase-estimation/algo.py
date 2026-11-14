import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFTGate
from qlab import counts, out, save_circuit, save_curve, save_hist


def qpe(theta, n):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n))
    for j in range(n):
        qc.cp(2 * np.pi * theta * 2**j, j, n)
    qc.append(QFTGate(n).inverse(), range(n))
    qc.measure(range(n), range(n))
    return qc


def estimate(theta, n):
    c = counts(qpe(theta, n), shots=4096)
    k = int(max(c, key=c.get), 2)
    return k / 2**n, c


def main():
    d = out(__file__)
    e, c = estimate(1 / 8, 3)
    print(f"theta=1/8 n=3 -> estimate {e} (exact, probability {c.get('001', 0) / 4096:.3f})")
    e, c = estimate(1 / 3, 6)
    print(f"theta=1/3 n=6 -> estimate {e:.6f} error {abs(e - 1 / 3):.6f}")
    save_hist(c, d / "histogram.png", "QPE theta=1/3, n=6 counting qubits")
    save_circuit(qpe(1 / 8, 3), d / "circuit.png")
    ns = np.arange(2, 10)
    err = [abs(estimate(1 / 3, int(n))[0] - 1 / 3) for n in ns]
    for n, x in zip(ns, err):
        print(f"n={n} error={x:.6f} bound 2^-(n+1)={2.0 ** -(n + 1):.6f}")
    save_curve(
        [("measured error", ns, err, "o-"), ("bound 2^-(n+1)", ns, 2.0 ** -(ns + 1), "s--")],
        d / "error_vs_n.png",
        "QPE precision vs counting qubits",
        "n",
        "|theta - estimate|",
        logy=True,
    )


if __name__ == "__main__":
    main()

