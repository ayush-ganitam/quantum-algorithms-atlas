import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import numpy as np
from qiskit import QuantumCircuit
from qlab import counts, out, save_circuit, save_curve, save_hist


def oracle(a):
    n = len(a)
    qc = QuantumCircuit(n + 1)
    for i, bit in enumerate(a[::-1]):
        if bit == "1":
            qc.cx(i, n)
    return qc


def bv(a):
    n = len(a)
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    qc.barrier()
    qc.compose(oracle(a), inplace=True)
    qc.barrier()
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc


def recover(a):
    c = counts(bv(a), shots=256)
    return max(c, key=c.get), c


def main():
    d = out(__file__)
    rng = np.random.default_rng(3)
    for n in (3, 6, 10):
        a = "".join(map(str, rng.integers(0, 2, n)))
        found, c = recover(a)
        print(f"n={n:2d} secret={a} found={found} one query, outcomes={len(c)} ok={a == found}")
    a = "101101"
    found, c = recover(a)
    save_hist(c, d / "histogram.png", f"hidden string a = {a}")
    save_circuit(bv(a), d / "circuit.png")
    ns = np.arange(1, 21)
    save_curve(
        [("classical: n queries", ns, ns, "o-"), ("quantum: 1 query", ns, np.ones_like(ns), "s-")],
        d / "queries.png",
        "Queries needed to find the hidden string",
        "n (bits in a)",
        "oracle queries",
    )


if __name__ == "__main__":
    main()

