# 11. Hamiltonian Simulation and QPE Energy Estimation

**Intuition.** Feynman's original reason for quantum computers: to simulate quantum physics you need a quantum system. To advance a system through time you cut the evolution into tiny slices and apply each physical interaction in turn (Trotterization). Feeding that evolution into phase estimation then reads out the system's energies.

**Problem.** Given H and time t, implement |ψ(t)> = e^(-iHt)|ψ(0)>.

**Formulas**
- Lie-Trotter: e^(-iHt) ≈ (Π_k e^(-iH_k t/r))^r, per-step error O((t/r)² Σ_{j<k} ||[H_j, H_k]||), total error O(t²/r)
- Second-order (Suzuki) formula: total error O(t³/r²)
- Eigenstate phase: e^(-iHt)|E_j> = e^(-iE_j t)|E_j>
- QPE with U = e^(-iHt) returns φ with e^(2πiφ) = e^(-iE t), so **φ = -E·t/2π (mod 1)** and **E = -2πφ/t**, valid when |E|·t < 2π
- Energy resolution: 2π / (t · 2^n)

**Corrected sign.** Many texts write E = +2πφ/t with U = e^(-iHt); that has the wrong sign. The code uses the correct one.

**In the code.** Part A simulates a 3-qubit transverse-field Ising chain H = -Σ Z_i Z_{i+1} - 0.8 Σ X_i and compares Lie and Suzuki Trotter circuits with exact evolution. Part B runs QPE on the H2 Hamiltonian from chapter 10 using the exact unitary e^(-iHt) (instead of Trotterised) to isolate QPE accuracy, with t = 2 and n = 6.

**QPE vs VQE.** QPE gives energies limited only by n and Trotter error but needs deep, fault-tolerant circuits and a good eigenstate overlap. VQE uses shallow circuits but gives only a variational upper bound.

**Applications.** Chemistry and materials, nuclear and particle physics, and quantum field theory; the flagship long-term quantum application.

