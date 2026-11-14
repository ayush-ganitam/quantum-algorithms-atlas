from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


def out(f):
    d = Path(f).resolve().parent / "output"
    d.mkdir(exist_ok=True)
    return d


def counts(qc, shots=4096, seed=7):
    sim = AerSimulator(seed_simulator=seed)
    job = sim.run(transpile(qc, sim, seed_transpiler=seed), shots=shots)
    return job.result().get_counts()


def save_hist(c, path, title=""):
    fig = plot_histogram(c, title=title, figsize=(8, 4))
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def save_circuit(qc, path, fold=-1):
    fig = qc.draw("mpl", fold=fold)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def save_grid(items, path, cols=2):
    rows = -(-len(items) // cols)
    fig, axs = plt.subplots(rows, cols, figsize=(5 * cols, 3.4 * rows), squeeze=False)
    for ax, (title, c) in zip(axs.ravel(), items):
        plot_histogram(c, ax=ax, title=title)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def save_curve(series, path, title, xlabel, ylabel, logx=False, logy=False):
    fig, ax = plt.subplots(figsize=(7, 4))
    for label, xs, ys, style in series:
        ax.plot(xs, ys, style, label=label)
    if logx:
        ax.set_xscale("log")
    if logy:
        ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.3)
    ax.legend()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)

