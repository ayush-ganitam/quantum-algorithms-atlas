# 02. Deutsch's Algorithm

**Intuition.** A hidden function takes one bit in and gives one bit out. You must decide whether it ignores its input (constant) or really depends on it (balanced). Classically you must evaluate it twice. A quantum computer asks once, about both inputs at the same time, and reads the answer from an interference pattern.

**Problem.** Given an oracle f: {0,1} → {0,1} promised to be constant (f(0) = f(1)) or balanced (f(0) ≠ f(1)), decide which using the fewest queries.

**Oracle.** U_f |x>|y> = |x>|y ⊕ f(x)>

**Derivation (formulas)**
1. |ψ0> = |0>|1>
2. |ψ1> = [(|0>+|1>)/√2] ⊗ [(|0>-|1>)/√2]
3. Phase kickback: U_f |x>(|0>-|1>)/√2 = (-1)^f(x) |x>(|0>-|1>)/√2
4. |ψ2> = [((-1)^f(0)|0> + (-1)^f(1)|1>)/√2] ⊗ [(|0>-|1>)/√2]
5. Apply H to qubit 1. If constant, the result is ±|0>. If balanced, it is ±|1>.
6. Measure qubit 1. Outcome 0 means constant; outcome 1 means balanced.

**Complexity.** Classical: 2 queries. Quantum: 1 query, deterministic.

**Note on history.** Deutsch (1985) introduced the idea. The deterministic one-query form is due to Deutsch-Jozsa (1992) and Cleve et al. (1998).

**Applications.** The standard first example of quantum advantage. Its phase-kickback trick is reused in Bernstein-Vazirani, Simon, Shor, and QPE.

