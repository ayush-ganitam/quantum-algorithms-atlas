# 03. Bernstein-Vazirani Algorithm

**Intuition.** A secret n-bit code a is hidden inside a box. The box answers a·x (the XOR of the bits of a selected by x). Classically you learn one bit of a per question, so n questions. A quantum computer reads the whole code with one question.

**Problem.** Given f(x) = a·x (mod 2) = a1x1 ⊕ ... ⊕ anxn, find the hidden string a.

**Derivation (formulas)**
1. Start: |0>^n |1>
2. After H on all qubits: (1/√(2^n)) Σ_x |x> ⊗ (|0>-|1>)/√2
3. After oracle (phase kickback): (1/√(2^n)) Σ_x (-1)^(a·x) |x> ⊗ (|0>-|1>)/√2
4. Apply H^⊗n using H^⊗n|x> = (1/√(2^n)) Σ_z (-1)^(x·z)|z>. Every term cancels except z = a.
5. Final state: |a> ⊗ |->. Measuring the first n qubits gives a with probability 1.

**Complexity.** Classical: n queries. Quantum: 1 query.

**Applications.** Teaches the general n-qubit phase-kickback pattern; the same structure appears in learning hidden linear structure.

