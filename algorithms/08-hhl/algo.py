import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.circuit.library import HamiltonianGate, QFTGate, RYGate
from qlab import counts, out, save_circuit

A = np.array([[1, -1 / 3], [-1 / 3, 1]])
B = np.array([0.0, 1.0])
T = 3 * np.pi / 4


def cu(j, s):
    return HamiltonianGate(A, -s * T * 2**j).control(1)


def forward(qc):
    qc.h([1, 2])
    for j in range(2):
        qc.append(cu(j, 1), [1 + j, 3])
    qc.append(QFTGate(2).inverse(), [1, 2])


def backward(qc):
    qc.append(QFTGate(2), [1, 2])
    for j in reversed(range(2)):
        qc.append(cu(j, -1), [1 + j, 3])
    qc.h([1, 2])


def rotate(qc):
    for k in (1, 2):
        qc.append(RYGate(2 * np.arcsin(1 / k)).control(2, ctrl_state=k), [1, 2, 0])


def hhl():
    qc = QuantumCircuit(4)
    qc.x(3)
    forward(qc)
    qc.barrier()
    rotate(qc)
    qc.barrier()
    backward(qc)
    return qc


def run(shots=40000):
    qc = hhl()
    qc.measure_all()
    c = counts(qc, shots=shots)
    keep = {k: v for k, v in c.items() if k[-1] == "1" and k[1:3] == "00"}
    tot = sum(keep.values())
    p = [sum(v for k, v in keep.items() if k[0] == b) / tot for b in "01"]
    return p, tot / shots


def main():
    d = out(__file__)
    x = np.linalg.solve(A, B)
    pc = (x / np.linalg.norm(x)) ** 2
    pq, ok = run()
    print("eigenvalues of A:", np.round(np.linalg.eigvalsh(A), 4))
    print("classical solution x:", np.round(x, 4))
    print("classical |x_i|^2 normalised:", np.round(pc, 4))
    print("HHL postselected |x_i|^2   :", np.round(pq, 4))
    print("ancilla success probability:", round(ok, 4))
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.bar(np.arange(2) - 0.18, pc, 0.36, label="classical A^-1 b")
    ax.bar(np.arange(2) + 0.18, pq, 0.36, label="HHL circuit")
    ax.set_xticks([0, 1], ["|x0|^2", "|x1|^2"])
    ax.legend()
    ax.set_title("HHL vs classical solution")
    fig.savefig(d / "solution.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    save_circuit(hhl(), d / "circuit.png")


if __name__ == "__main__":
    main()

