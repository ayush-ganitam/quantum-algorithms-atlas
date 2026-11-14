import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qlab import counts, out, save_circuit, save_curve, save_hist


def oracle(t):
    n = len(t)
    qc = QuantumCircuit(n)
    z = [i for i, b in enumerate(t[::-1]) if b == "0"]
    if z:
        qc.x(z)
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    if z:
        qc.x(z)
    return qc


def diffuser(n):
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))
    return qc


def grover(t, k, meas=True):
    n = len(t)
    qc = QuantumCircuit(n, n if meas else 0)
    qc.h(range(n))
    for _ in range(k):
        qc.barrier()
        qc.compose(oracle(t), inplace=True)
        qc.compose(diffuser(n), inplace=True)
    if meas:
        qc.measure(range(n), range(n))
    return qc


def prob(t, k):
    return Statevector(grover(t, k, False)).probabilities_dict().get(t, 0.0)


def main():
    d = out(__file__)
    t = "1011"
    n = len(t)
    N = 2**n
    k = int(np.pi / 4 * np.sqrt(N))
    print(f"N={N} target={t} optimal iterations k={k}")
    c = counts(grover(t, k), shots=4096)
    print("top outcome:", max(c, key=c.get), "P =", round(c[t] / 4096, 4))
    theta = np.arcsin(1 / np.sqrt(N))
    ks = np.arange(0, 9)
    sim = [prob(t, int(i)) for i in ks]
    thy = np.sin((2 * ks + 1) * theta) ** 2
    for i in ks:
        print(f"k={i} simulated={sim[i]:.4f} theory={thy[i]:.4f}")
    save_hist(c, d / "histogram.png", f"Grover N={N}, target {t}, k={k}")
    save_curve(
        [("simulated", ks, sim, "o-"), ("sin^2((2k+1)theta)", ks, thy, "s--")],
        d / "probability_vs_k.png",
        "Success probability vs Grover iterations",
        "k",
        "P(target)",
    )
    save_circuit(grover(t, 1), d / "circuit.png")


if __name__ == "__main__":
    main()

