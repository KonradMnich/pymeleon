"""The module demonstrates how to store a matplotlib figure for later usage
and how to read it back to the program.
"""
import matplotlib.pyplot as plt
from pymeleon.figure_storage import store_figure, read_figure


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.plot([0, 1], [2, 3])
    plt.show()
    store_figure(fig, "my_fig")
    fig2 = read_figure("my_fig")
    fig2.show()
