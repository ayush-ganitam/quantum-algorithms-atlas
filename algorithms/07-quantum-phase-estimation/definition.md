# 07. Quantum Phase Estimation (QPE)

**Intuition.** Some quantum operations leave a state unchanged except for a twist (a phase). QPE measures that twist as a binary fraction. It is not an end-user algorithm; it is the measuring tool inside Shor, HHL, and quantum chemistry.

**Problem.** Given a unitary U and an eigenvector |ψ> with U|ψ> = e^(2πiθ)|ψ>, estimate θ ∈ [0, 1) to n bits.

**Derivation (formulas)**
1. (1/√(2^n)) Σ_k |k>|ψ>, after H on n counting qubits
2. Controlled-U^(2^j) from counting qubit j gives (1/√(2^n)) Σ_k e^(2πiθk) |k>|ψ>
3. Inverse QFT maps this register to |θ̃>
4. Measure to get θ̃ ≈ k/2^n

**Precision.** If θ = k/2^n exactly, the result is deterministic. Otherwise the nearest n-bit value is returned with probability at least 4/π², and the error is at most 2^-(n+1) for that nearest value.

**Applications.** Core of Shor, HHL, and Hamiltonian-simulation energy estimation; generalised by quantum singular value transformation.

