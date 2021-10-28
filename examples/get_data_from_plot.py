"""This module demonstrates how to get the tabular data from a figure."""
from graph_scraping import scrap_data
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fig, ax = plt.subplots(2, 2)
    ax[0, 0].plot([1, 2, 3], [4, 5, 7])
    ax[0, 0].plot([1.1, 2.1, 3.1, 4.1], [7.1, 5.1, 4.1, 3.1])
    ax[0, 1].plot([100, 200], [10, 10])
    ax[0, 1].plot([100, 200], [-1, -1])
    ax[1, 0].plot([1, 2, 3], [4, 5, 7])
    ax[1, 0].plot([1.1, 2.1, 3.1, 4.1], [7.1, 5.1, 4.1, 3.1])
    ax[1, 1].plot([100, 200], [10, 10])
    ax[1, 1].plot([100, 200], [-1, -1])
    plt.show()

    df = scrap_data(fig)
    print(df)
