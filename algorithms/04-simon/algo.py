import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import numpy as np
from qiskit import QuantumCircuit
from qlab import counts, out, save_circuit, save_curve, save_hist


def oracle(s):
    n = len(s)
    s = s[::-1]
    qc = QuantumCircuit(2 * n)
    for q in range(n):
        qc.cx(q, n + q)
    if "1" in s:
        i = s.index("1")
        for q in range(n):
            if s[q] == "1":
                qc.cx(i, n + q)
    return qc


def simon(s):
    n = len(s)
    qc = QuantumCircuit(2 * n, n)
    qc.h(range(n))
    qc.barrier()
    qc.compose(oracle(s), inplace=True)
    qc.barrier()
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc


def dot(a, b):
    return bin(a & b).count("1") % 2


def solve(ys, n):
    return [c for c in range(1, 2**n) if all(dot(c, y) == 0 for y in ys)]


def main():
    d = out(__file__)
    s = "110"
    n = len(s)
    c = counts(simon(s), shots=2048)
    ys = sorted({int(k, 2) for k in c})
    print("hidden s =", s)
    print("measured y:", [format(y, f"0{n}b") for y in ys])
    print("all y.s = 0:", all(dot(y, int(s, 2)) == 0 for y in ys))
    print("candidates consistent with every y:", [format(x, f"0{n}b") for x in solve(ys, n)])
    save_hist(c, d / "histogram.png", f"Simon n={n}, s={s}: only y with y.s=0 appear")
    save_circuit(simon(s), d / "circuit.png")
    ns = np.arange(2, 25)
    save_curve(
        [("classical ~ 2^(n/2)", ns, 2 ** (ns / 2), "o-"), ("quantum ~ n", ns, ns, "s-")],
        d / "queries.png",
        "Simon's problem: query growth",
        "n",
        "queries",
        logy=True,
    )


if __name__ == "__main__":
    main()

