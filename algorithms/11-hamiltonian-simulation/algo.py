import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))
import numpy as np
from scipy.linalg import expm
from qiskit import QuantumCircuit
from qiskit.circuit.library import HamiltonianGate, PauliEvolutionGate, QFTGate
from qiskit.circuit.library import StatePreparation
from qiskit.quantum_info import SparsePauliOp, Statevector
from qiskit.synthesis import LieTrotter, SuzukiTrotter
from qlab import counts, out, save_circuit, save_curve, save_hist

TFIM = SparsePauliOp.from_list([("ZZI", -1), ("IZZ", -1), ("XII", -0.8), ("IXI", -0.8), ("IIX", -0.8)])
H2 = SparsePauliOp.from_list(
    [
        ("II", -1.052373245772859),
        ("IZ", 0.39793742484318045),
        ("ZI", -0.39793742484318045),
        ("ZZ", -0.01128010425623538),
        ("XX", 0.18093119978423156),
    ]
)


def exact(t):
    v = np.zeros(8, complex)
    v[0] = 1
    return expm(-1j * np.asarray(TFIM.to_matrix(sparse=False)) * t) @ v


def trotter(t, r, order):
    syn = LieTrotter(reps=r) if order == 1 else SuzukiTrotter(order=2, reps=r)
    qc = QuantumCircuit(3)
    qc.append(PauliEvolutionGate(TFIM, time=t, synthesis=syn), range(3))
    return qc.decompose(reps=2)


def infid(t, r, order):
    s = Statevector(trotter(t, r, order)).data
    return 1 - abs(np.vdot(exact(t), s)) ** 2


def mag(v):
    return float(Statevector(v).expectation_value(SparsePauliOp("IIZ")).real)


def qpe_energy(n=6, t=2.0):
    w, v = np.linalg.eigh(H2.to_matrix())
    m = H2.to_matrix()
    qc = QuantumCircuit(n + 2, n)
    qc.append(StatePreparation(v[:, 0]), [n, n + 1])
    qc.h(range(n))
    for j in range(n):
        qc.append(HamiltonianGate(m, t * 2**j).control(1), [j, n, n + 1])
    qc.append(QFTGate(n).inverse(), range(n))
    qc.measure(range(n), range(n))
    c = counts(qc, shots=4096)
    k = int(max(c, key=c.get), 2)
    return -2 * np.pi * (k / 2**n) / t, w[0], c, qc


def main():
    d = out(__file__)
    rs = np.array([1, 2, 4, 8, 16, 32])
    e1 = [infid(1.0, int(r), 1) for r in rs]
    e2 = [infid(1.0, int(r), 2) for r in rs]
    for r, a, b in zip(rs, e1, e2):
        print(f"steps={r:2d} infidelity Lie={a:.2e} Suzuki2={b:.2e}")
    save_curve(
        [("Lie-Trotter (order 1)", rs, e1, "o-"), ("Suzuki (order 2)", rs, e2, "s-")],
        d / "trotter_error.png",
        "Trotter infidelity vs steps (t=1)",
        "steps r",
        "1 - fidelity",
        True,
        True,
    )
    ts = np.linspace(0.05, 4, 40)
    ex = [mag(exact(t)) for t in ts]
    tr = [mag(Statevector(trotter(t, int(np.ceil(6 * t)), 2)).data) for t in ts]
    save_curve(
        [("exact", ts, ex, "-"), ("Suzuki order 2", ts, tr, "o")],
        d / "dynamics.png",
        "Transverse-field Ising chain: <Z0>(t)",
        "t",
        "<Z0>",
    )
    est, ex_e, c, qc = qpe_energy()
    print(f"QPE energy estimate : {est:.4f}")
    print(f"exact ground energy : {ex_e:.4f}")
    print(f"resolution 2*pi/(t*2^n) = {2 * np.pi / (2 * 2**6):.4f}")
    save_hist(c, d / "qpe_energy.png", "QPE on e^{-iHt}, H2 ground state")
    save_circuit(trotter(0.5, 2, 1), d / "circuit.png")


if __name__ == "__main__":
    main()

