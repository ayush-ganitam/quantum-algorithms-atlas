# 01. Hadamard Gate, Superposition and Interference

**Intuition (no prerequisites).** A normal bit is 0 or 1. A qubit can be a blend of both. The Hadamard gate turns a definite bit into a 50/50 blend. Applied twice, the two paths recombine and the original bit returns, because quantum numbers can cancel each other. That cancelling is where every quantum speedup comes from.

**Formal definition.** The Hadamard gate is the unitary H = (1/√2)[[1, 1], [1, -1]], Hermitian with H = H† and H² = I.

**Formulas**
- H|0> = (|0> + |1>)/√2 = |+>
- H|1> = (|0> - |1>)/√2 = |->
- General qubit: |ψ> = α|0> + β|1>, with |α|² + |β|² = 1.
- P(0) = |α|², P(1) = |β|²
- H^⊗n |0...0> = (1/√(2^n)) Σ_x |x>
- H^⊗n |x> = (1/√(2^n)) Σ_z (-1)^(x·z) |z>

**Key observation.** |+> and |-> give identical measurement statistics, so the sign is invisible. A second H turns that sign into a deterministic outcome: H|+> = |0> and H|-> = |1>. This is interference.

**Applications.** First step of nearly every algorithm; quantum random number generators.

