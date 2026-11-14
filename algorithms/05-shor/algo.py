import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
from math import gcd
from fractions import Fraction
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFTGate
from qlab import counts, out, save_circuit, save_hist

N = 15
SWAPS = {
    2: [(2, 3), (1, 2), (0, 1)],
    7: [(1, 2), (2, 3), (0, 3)],
    8: [(0, 1), (1, 2), (2, 3)],
    11: [(1, 3), (0, 2)],
    13: [(2, 3), (1, 2), (0, 1)],
}


def mult(a, p):
    qc = QuantumCircuit(4)
    for _ in range(p % 4):
        for i, j in SWAPS[a]:
            qc.swap(i, j)
        if a in (7, 11, 13):
            qc.x([0, 1, 2, 3])
    g = qc.to_gate()
    g.name = f"{a}^{p} mod 15"
    return g.control()


def shor_circuit(a, m):
    qc = QuantumCircuit(m + 4, m)
    qc.h(range(m))
    qc.x(m)
    for j in range(m):
        qc.append(mult(a, 2**j), [j] + list(range(m, m + 4)))
    qc.append(QFTGate(m).inverse(), range(m))
    qc.measure(range(m), range(m))
    return qc


def factors(a, k, m):
    r = Fraction(k, 2**m).limit_denominator(N).denominator
    if r % 2 or pow(a, r, N) != 1 or pow(a, r // 2, N) == N - 1:
        return r, None
    h = pow(a, r // 2, N)
    return r, sorted({gcd(h - 1, N), gcd(h + 1, N)} - {1, N})


def attempt(a, m=8):
    c = counts(shor_circuit(a, m), shots=1024)
    for key in sorted(c, key=c.get, reverse=True):
        r, f = factors(a, int(key, 2), m)
        if f:
            return c, int(key, 2), r, f
    return c, None, None, None


def main():
    d = out(__file__)
    m = 8
    for a in (7, 11, 13, 2, 8):
        c, k, r, f = attempt(a, m)
        print(f"a={a:2d} measured k={k} phase={k}/{2**m} period r={r} factors of {N}: {f}")
    c, *_ = attempt(7, m)
    save_hist(c, d / "histogram.png", "Shor N=15, a=7: peaks at k = 0, 64, 128, 192 (multiples of 2^m / r)")
    save_circuit(shor_circuit(7, m), d / "circuit.png")


if __name__ == "__main__":
    main()

