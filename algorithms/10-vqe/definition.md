# 10. Variational Quantum Eigensolver (VQE)

**Intuition.** Nature settles into its lowest-energy state. VQE guesses a quantum state with adjustable knobs, measures its energy, and lets a classical optimiser turn the knobs downhill. The variational principle guarantees you can never dip below the true answer, so lower always means closer.

**Problem.** Find the ground-state energy E0 of a Hamiltonian H (here, molecular hydrogen).

**Formulas**
- Variational principle: <ψ(θ)|H|ψ(θ)> ≥ E0 for every normalised |ψ(θ)>
- Pauli decomposition: H = Σ_k c_k P_k, with P_k ∈ {I, X, Y, Z}^⊗n
- Energy: E(θ) = Σ_k c_k <P_k>
- Loop: prepare |ψ(θ)>, measure each <P_k>, sum classically, update θ, repeat until converged.

**H2 instance (0.735 Å, 2-qubit reduced form).** H = -1.0524 II + 0.3979 IZ - 0.3979 ZI - 0.0113 ZZ + 0.1809 XX (Hartree, electronic part). Total energy = electronic + nuclear repulsion 0.71997 Ha. The 6-parameter ansatz uses RY layers with two CNOTs, which spans all real 2-qubit states.

**Applications.** Molecular and materials energies, catalyst and drug design; the most widely run quantum chemistry algorithm on current hardware.

