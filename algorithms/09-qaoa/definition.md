# 09. Quantum Approximate Optimization Algorithm (QAOA)

**Intuition.** Many real problems ask for the best choice among exponentially many (route planning, scheduling, splitting a network). QAOA encodes the problem as an energy landscape and alternates two moves: "reward good answers" and "shake things up". A classical computer tunes how strong each move is, and the quantum computer tests the result. It is built for today's noisy hardware.

**Problem (Max-Cut).** Split the vertices of a graph into two groups to maximise the number of edges between groups.

**Formulas**
- Cost Hamiltonian: Hc = Σ_{(i,j)∈E} (1 - Z_i Z_j)/2 (its expectation is the cut value, which we maximise)
- Mixer: Hb = Σ_i X_i
- Ansatz: |γ,β> = Π_{l=p..1} e^(-iβ_l Hb) e^(-iγ_l Hc) |+>^⊗n
- Objective: maximise <γ,β| Hc |γ,β>
- Hybrid loop: the quantum device prepares the state and estimates <Hc>; a classical optimiser (COBYLA) updates (γ, β).

**Depth trade-off.** Larger p gives a better approximation but a deeper, noisier circuit.

**Instance in the code.** 5 vertices, edges (0,1), (1,2), (2,3), (3,4), (4,0), (0,2); p = 2; best of 5 random restarts. Optimisation uses exact statevector expectations; final sampling uses the Aer simulator.

**Applications.** Max-Cut, graph partitioning, portfolio optimisation, routing, and scheduling; a leading NISQ-era candidate.

