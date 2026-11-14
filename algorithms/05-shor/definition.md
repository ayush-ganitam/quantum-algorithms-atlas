# 05. Shor's Algorithm

**Intuition.** Factoring a big number is hard because nobody knows a fast way to find its factors. Shor noticed it reduces to finding the repeat length of the sequence a^x mod N, and a quantum computer can find a repeat length quickly by making all the values interfere. Multiplying and dividing the repeat length into the number then reveals the factors.

**Problem.** Given a composite integer N, find a nontrivial factor.

**Reduction to period finding.** Choose a coprime to N and let f(x) = a^x mod N. Let r be the smallest r > 0 with a^r ≡ 1 (mod N).

**Algorithm (formulas)**
1. Pick random a with 1 < a < N. If gcd(a, N) > 1, a factor is found.
2. Build (1/√Q) Σ_x |x>|0>, with Q = 2^m.
3. Modular exponentiation: (1/√Q) Σ_x |x>|a^x mod N>
4. Apply the inverse QFT. QFT|x> = (1/√Q) Σ_k e^(2πi·xk/Q) |k>. The register peaks at k ≈ j·Q/r for integer j.
5. Continued fractions on k/Q recover r.
6. If r is odd or a^(r/2) ≡ -1 (mod N), retry with a new a.
7. Otherwise gcd(a^(r/2) - 1, N) and gcd(a^(r/2) + 1, N) give nontrivial factors.

**Worked example (N = 15, a = 7).** 7^x mod 15 = 7, 4, 13, 1, 7, ... so r = 4. Then 7² mod 15 = 4, gcd(3, 15) = 3 and gcd(5, 15) = 5.

**Complexity.** Quantum: O((log N)² log log N log log log N). Classical best known: exp(O((log N)^(1/3) (log log N)^(2/3))).

**Applications.** Breaks RSA, Diffie-Hellman, and elliptic-curve cryptography, which drives the migration to post-quantum cryptography.

**Code note.** The modular multiplication circuits are hard-coded for N = 15 (the standard textbook construction), so the quantum circuit is real but small-scale. Larger N needs general modular arithmetic circuits.

