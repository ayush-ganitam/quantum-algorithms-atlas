# Quantum Algorithms Atlas: From Unitary Primitives to Trotterized Hamiltonian Simulation

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Qiskit 2.6.2](https://img.shields.io/badge/Qiskit-2.6.2-6929C4?style=flat-square&logo=qiskit&logoColor=white)](https://www.ibm.com/quantum/qiskit)
[![Qiskit Aer 0.18.2](https://img.shields.io/badge/Qiskit_Aer-0.18.2-00539A?style=flat-square)](https://qiskit.github.io/qiskit-aer/)
[![CI Automated Verification](https://img.shields.io/badge/CI-Automated_Aer_Verification-2EA44F?style=flat-square&logo=githubactions&logoColor=white)](.github/workflows/build.yml)
<br>

## Academic Mentorship & Attribution

<table>
  <tr>
    <td>
      Developed by <a href="#author--mentor-profiles"><strong>Ayush Kumar</strong></a> under the esteemed guidance and mentorship of <a href="#author--mentor-profiles"><strong>Dr. N. S. Vidhyadhiraja</strong></a>, Professor and Chair, Theoretical Sciences Unit, <strong>Jawaharlal Nehru Centre for Advanced Scientific Research (JNCASR), Bengaluru</strong>.
    </td>
  </tr>
</table>

Driven by a deep commitment to quantum information science, quantum algorithm design, and mathematical rigor, **Ayush Kumar** approaches quantum computation from first principles—translating unitary operator theory, spectral decomposition, and interference mechanics into verified, executable quantum circuits aimed at advancing scientific understanding and positive real-world impact. Alongside direct academic guidance from **Dr. N. S. Vidhyadhiraja** in quantum mechanics, strongly correlated systems, and computational physics, the architectural ideas and derivations in this repository draw active inspiration from **IBM Quantum Lectures** (including the *Fundamentals of Quantum Algorithms* series), selective reference to **John Watrous's** treatise ***The Theory of Quantum Information*** for operator-theoretic and formalism foundations, and foundational peer-reviewed research literature across quantum computing.

<br>

## Abstract & Vision

**Quantum Algorithms Atlas** is a rigorous, end-to-end computational reference spanning eleven foundational quantum algorithms—progressing systematically from single-qubit unitary interference to fault-tolerant phase estimation, variational eigensolvers, and product-formula Hamiltonian dynamics.

Rather than treating quantum circuits as opaque black-box API calls, every chapter is engineered around **progressive technical disclosure**:

1. **Mathematical Formulation & State Evolution:** Explicit Hilbert-space transformations, unitary operator definitions, phase-kickback derivations, and asymptotic complexity bounds.
2. **Comment-Free Modular Qiskit Synthesis:** Clean, deterministic circuit construction written in native Qiskit 2.x (`Statevector`, `SparsePauliOp`, `PauliEvolutionGate`, `QFTGate`, and `StatevectorEstimator`).
3. **Verified Aer Simulator Telemetry:** Exact statevector amplitudes, finite-shot measurement histograms (`AerSimulator`), Trotter infidelity scaling curves, and circuit schematics generated and verified automatically via Continuous Integration.

<br>

## Complete Algorithm Index & Technical Specification Matrix

Start at **Chapter 01** and progress sequentially. Click any algorithm below to inspect its formal derivation, followed by expandable tabs for its Qiskit 2.x implementation and verified simulator telemetry.

| # | Algorithm | Core Quantum Mechanism & Unitary | Problem Solved | Quantum Complexity | Classical Bound | Hardware Regime | Verified Simulator Benchmark |
|:-:|:---|:---|:---|:---|:---|:---|:---|
| **01** | [Hadamard & Superposition](algorithms/01-hadamard-superposition) | Unitary involution $H = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1\\ 1 & -1\end{bmatrix}$, $H^2 = I$, Walsh–Hadamard transform $H^{\otimes n}$ | Constructive/destructive amplitude interference & uniform superposition | $O(1)$ circuit depth | $O(2^n)$ state-vector memory | Universal Primitive | $H\Vert{}0\rangle, H\Vert{}1\rangle \rightarrow 50/50$; $H^2\Vert{}x\rangle \rightarrow \Vert{}x\rangle$ ($100\%$) |
| **02** | [Deutsch's Algorithm](algorithms/02-deutsch) | Phase kickback $U_f\Vert{}x\rangle\Vert{}-\rangle = (-1)^{f(x)}\Vert{}x\rangle\Vert{}-\rangle$ + Hadamard interference | Determine whether $f:\{0,1\}\to\{0,1\}$ is constant or balanced | $1$ oracle query | $2$ queries (deterministic) | NISQ / Educational | Constant $\rightarrow \Vert{}0\rangle$, Balanced $\rightarrow \Vert{}1\rangle$ ($1024/1024$ shots) |
| **03** | [Bernstein–Vazirani](algorithms/03-bernstein-vazirani) | $n$-qubit phase kickback + Fourier sampling over $\mathbb{F}_2^n$ | Extract hidden bitstring $a \in \{0,1\}^n$ from $f(x) = a \cdot x \pmod 2$ | $1$ oracle query | $n$ queries | NISQ | Exact recovery for $n \in \{3, 6, 10\}$ in $1$ query ($100\%$) |
| **04** | [Simon's Algorithm](algorithms/04-simon) | Abelian hidden subgroup sampling + orthogonal subspace $y \cdot s = 0 \pmod 2$ | Find hidden period $s \neq 0$ where $f(x) = f(x \oplus s)$ | $O(n)$ queries + $O(n^3)$ $\text{GF}(2)$ elimination | $\Theta(2^{n/2})$ (birthday bound) | Fault-Tolerant (FTQC) | $s=110 \rightarrow \{000, 001, 110, 111\}$ strictly ($y \cdot s = 0$) |
| **05** | [Shor's Algorithm](algorithms/05-shor) | Controlled modular exponentiation $\Vert{}x\rangle\Vert{}a^x \bmod N\rangle$ + $\text{QFT}^\dagger$ + continued fractions | Integer factorization via multiplicative order finding $a^r \equiv 1 \pmod N$ | $O((\log N)^2 \log\log N \log\log\log N)$ | $\exp\!\left(O((\log N)^{1/3}(\log\log N)^{2/3})\right)$ | Fault-Tolerant (FTQC) | $N=15$, $a \in \{2,7,8,11,13\} \rightarrow$ factors $[3, 5]$ |
| **06** | [Grover's Search](algorithms/06-grover) | $\text{SU}(2)$ invariant-subspace rotation $G = (2\Vert{}s\rangle\langle s\Vert{} - I)O_f$ | Unstructured search for marked state $w$ among $N = 2^n$ items | $O(\sqrt{N})$ queries ($k \approx \frac{\pi}{4}\sqrt{N}$) | $\Theta(N)$ | FTQC / Early FTQC | $N=16, w=1011, k=3 \rightarrow P(w)=0.9613$ ($\sin^2((2k+1)\theta)$) |
| **07** | [Quantum Phase Estimation](algorithms/07-quantum-phase-estimation) | Controlled-$U^{2^j}$ phase encoding + inverse Quantum Fourier Transform ($\text{QFT}^\dagger$) | Estimate eigenphase $\theta \in [0,1)$ of $U\Vert{}\psi\rangle = e^{2\pi i\theta}\Vert{}\psi\rangle$ to $n$ bits | $O(1/\epsilon)$ controlled-$U$ ops | Exponential in system dimension | Fault-Tolerant (FTQC) | $\theta=\frac{1}{8}$ exact ($1.000$); $\theta=\frac{1}{3}, n=6 \rightarrow 0.328125$ ($<2^{-(n+1)}$) |
| **08** | [HHL Linear Solver](algorithms/08-hhl) | QPE on $e^{iAt}$ + controlled-$R_y(2\arcsin(C/\lambda_j))$ + QPE uncomputation | Prepare quantum state $\Vert{}x\rangle \propto A^{-1}\Vert{}b\rangle$ for sparse Hermitian $A$ | $O(\log(N)\, s^2 \kappa^2 / \epsilon)$ | $O(N s \kappa)$ (Conjugate Gradient) | Fault-Tolerant (FTQC) | $\Vert{}x\Vert{}^2 = [0.1035, 0.8965]$ vs. classical $[0.1, 0.9]$ ($P_{\text{anc}}=0.628$) |
| **09** | [QAOA (Max-Cut)](algorithms/09-qaoa) | Alternating cost $e^{-i\gamma_l H_C}$ ($R_{ZZ}$) & mixer $e^{-i\beta_l H_B}$ ($R_X$) ansatz | Combinatorial graph partitioning maximizing cut edges $\sum_{(i,j)\in E}\frac{1-Z_i Z_j}{2}$ | $O(p\,\vert{}E\vert{})$ two-qubit gates | NP-Hard (APX-Hard) | NISQ | 5-node graph ($p=2$): ratio $0.9247$, optimal cut prob $0.7087$ |
| **10** | [VQE (Molecular $\text{H}_2$)](algorithms/10-vqe) | Rayleigh–Ritz principle $\langle\psi(\theta)\Vert{}H\Vert{}\psi(\theta)\rangle \ge E_0$ over Pauli strings | Ground-state electronic energy of $\text{H}_2$ ($0.735\text{ \AA}$, STO-3G) | Polynomial ansatz circuit depth | Exponential (Full CI) | NISQ | $E_{\text{elec}} = -1.857275\text{ Ha}$ (error $7.0\times 10^{-10}\text{ Ha}$) |
| **11** | [Hamiltonian Simulation](algorithms/11-hamiltonian-simulation) | 1st-order Lie-Trotter $O(t^2/r)$ & 2nd-order Suzuki $O(t^3/r^2)$ + QPE readout | Time evolution $\Vert{}\psi(t)\rangle = e^{-iHt}\Vert{}\psi(0)\rangle$ & spectral energy extraction | $\text{poly}(n, t, 1/\epsilon)$ | Exponential in qubit count $n$ | NISQ $\rightarrow$ FTQC | TFIM infidelity $1.98\times 10^{-7}$ ($r=32$); $\text{H}_2$ QPE $E=-1.8653\text{ Ha}$ |

---

## Architectural Design & Repository Layout

Every algorithm directory (`algorithms/01-*` through `algorithms/11-*`) maintains a strict separation between theoretical specification (`definition.md`) and quantum circuit execution (`algo.py`). Upon every push to `main`, a GitHub Actions runner executes `build_docs.py` in a clean Python 3.12 environment, validates numerical convergence against analytical bounds, renders high-DPI circuit and probability plots, and compiles interactive, collapsible `<details>` tabs inside each chapter's `README.md`.

```text
quantum-algorithms-atlas/
├── .github/workflows/build.yml        # Autonomous CI pipeline executing all 11 circuits
├── build_docs.py                      # Subprocess documentation & artifact compiler
├── requirements.txt                   # Pinned Qiskit 2.x, Aer, SciPy, and NumPy stack
├── qlab/
│   └── __init__.py                    # Deterministic Aer simulator & Matplotlib plotting engine
└── algorithms/
    ├── 01-hadamard-superposition/     # Unitary involution, Hadamard transform H^{\otimes n}, interference
    ├── 02-deutsch/                    # Single-query oracle parity & phase kickback
    ├── 03-bernstein-vazirani/         # Linear Boolean functional extraction over \mathbb{F}_2^n
    ├── 04-simon/                      # Abelian hidden subgroup & GF(2) orthogonal subspace sampling
    ├── 05-shor/                       # Modular exponentiation, inverse QFT & continued fractions
    ├── 06-grover/                     # SU(2) invariant-subspace rotation & amplitude amplification
    ├── 07-quantum-phase-estimation/   # Eigenphase binary readout & 2^{-(n+1)} precision scaling
    ├── 08-hhl/                        # Spectral decomposition, ancilla rotation & uncomputation
    ├── 09-qaoa/                       # Alternating Ising cost / transverse mixer ansatz (Max-Cut)
    ├── 10-vqe/                        # Rayleigh-Ritz variational ground-state estimation (H_2)
    └── 11-hamiltonian-simulation/     # Lie-Trotter O(t^2/r) vs. Suzuki O(t^3/r^2) & QPE readout
