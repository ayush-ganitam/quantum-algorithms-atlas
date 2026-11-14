# 04. Simon's Algorithm

**Intuition.** A box maps n-bit inputs to n-bit outputs, and secretly pairs up inputs: x and x⊕s always give the same output. Finding a collision classically needs about 2^(n/2) tries (birthday paradox). The quantum circuit instead produces random strings that are each guaranteed to be "perpendicular" to s. A handful of them pin s down.

**Problem.** Given f: {0,1}^n → {0,1}^n with f(x) = f(y) if and only if y = x ⊕ s for a hidden s ≠ 0, find s.

**Derivation (formulas)**
1. (1/√(2^n)) Σ_x |x>|0>, after H^⊗n on the first register
2. (1/√(2^n)) Σ_x |x>|f(x)>, after the oracle
3. Measuring the second register leaves (|x0> + |x0⊕s>)/√2
4. After H^⊗n, the amplitude of |y> is proportional to (-1)^(x0·y) [1 + (-1)^(s·y)]
5. This is nonzero only if s·y = 0 (mod 2). Each run returns a random y with y·s = 0.
6. Repeat about n-1 times, then solve the linear system over GF(2) for s.

**Complexity.** Classical: Θ(2^(n/2)) queries. Quantum: O(n) queries.

**Applications.** The first exponential query separation, and the direct precursor of Shor; basis of the abelian hidden-subgroup framework; quantum attacks on some symmetric constructions.

**Code note.** The solver brute-forces all nonzero candidates consistent with the equations, which is fine for small n; use Gaussian elimination over GF(2) at scale.

