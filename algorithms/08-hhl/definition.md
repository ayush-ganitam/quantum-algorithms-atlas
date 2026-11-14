# 08. HHL Algorithm (Quantum Linear Systems)

**Intuition.** To solve A·x = b, HHL splits b into the "natural directions" (eigenvectors) of A, divides each part by its eigenvalue, and recombines. The answer comes out as a quantum state, not a list of numbers, so it is useful only when you need a summary of x (an expectation value), not every entry.

**Problem.** Given Hermitian A (N×N, s-sparse, condition number κ) and |b>, prepare |x> ∝ A^-1|b>.

**Derivation (formulas)**
1. |b> = Σ_j β_j |u_j>, with A|u_j> = λ_j|u_j>
2. QPE with U = e^(iAt): Σ_j β_j |λ_j>|u_j>
3. Controlled rotation on an ancilla: Σ_j β_j |λ_j>|u_j> (√(1 - C²/λ_j²)|0> + (C/λ_j)|1>)
4. Uncompute QPE and post-select the ancilla on |1>: |x> ∝ Σ_j (β_j/λ_j)|u_j> = A^-1|b>

**Complexity.** Quantum: O(log N · s² · κ² / ε). Classical conjugate gradient: roughly O(N · s · κ). The speedup is exponential in N but comes with caveats: efficient state loading, sparse A, small κ, and only global properties of x are readable.

**Toy instance in the code.** A = [[1, -1/3], [-1/3, 1]], b = (0, 1). Eigenvalues are 2/3 and 4/3. With t = 3π/4 the phases are exactly 1/4 and 1/2, so a 2-qubit clock encodes them exactly (k = 1 and 2), and the rotation angle is 2·arcsin(1/k).

**Applications.** Foundation of many quantum machine learning speedup proposals and PDE solvers.

