import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
from qiskit import QuantumCircuit
from qlab import counts, out, save_circuit, save_grid

ORACLES = {
    "constant 0": [],
    "constant 1": [("x", 1)],
    "balanced identity": [("cx", 0, 1)],
    "balanced NOT": [("cx", 0, 1), ("x", 1)],
}


def oracle(ops):
    qc = QuantumCircuit(2)
    for op in ops:
        getattr(qc, op[0])(*op[1:])
    return qc


def deutsch(ops):
    qc = QuantumCircuit(2, 1)
    qc.x(1)
    qc.h([0, 1])
    qc.barrier()
    qc.compose(oracle(ops), inplace=True)
    qc.barrier()
    qc.h(0)
    qc.measure(0, 0)
    return qc


def verdict(c):
    return "CONSTANT" if c.get("0", 0) > c.get("1", 0) else "BALANCED"


def main():
    d = out(__file__)
    items = []
    for name, ops in ORACLES.items():
        c = counts(deutsch(ops), shots=1024)
        print(f"{name:18s} -> {dict(c)} -> {verdict(c)}")
        items.append((name, c))
    save_grid(items, d / "all_oracles.png")
    save_circuit(deutsch(ORACLES["balanced identity"]), d / "circuit_balanced.png")
    save_circuit(deutsch(ORACLES["constant 0"]), d / "circuit_constant.png")


if __name__ == "__main__":
    main()

