# 06. Grover's Algorithm

**Intuition.** Finding one marked item in an unsorted list of N items normally means checking about N/2 of them. Grover's algorithm starts with all items equally likely, then repeatedly nudges probability toward the marked one, like pushing a swing at the right moment. After about √N pushes, the marked item is almost certain. Push too long and it swings away again.

**Problem.** Given an oracle marking one item w among N = 2^n, find w.

**Operators (formulas)**
- Oracle: O_f|x> = -|x> if x = w, else |x>
- Diffusion: D = 2|s><s| - I, with |s> = (1/√N) Σ_x |x>
- Grover iteration: G = D·O_f
- Geometry: sin θ = 1/√N. After k iterations, the state sits at angle (2k+1)θ from the unmarked axis.
- Success probability: P(w) = sin²((2k+1)θ)
- Optimal iterations: k ≈ (π/4)√N

**Complexity.** Classical: O(N). Quantum: O(√N), provably optimal for unstructured search (BBBV theorem).

**Applications.** Speeds up any brute-force search (SAT, key search), and generalises to amplitude amplification and estimation. Against AES-256, Grover reduces effective strength to about 128 bits.

