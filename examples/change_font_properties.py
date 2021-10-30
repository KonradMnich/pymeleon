"""Change font properties of the elements of axis."""
from pymeleon.font_modifiers import *
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # create a plot
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.set_title("my title")
    ax.set_ylabel("my label")

    # modify the plot
    modify_font(ax, Location.XTICKS, Feature.COLOR, "olive")
    modify_multiple_elements(ax, "all", (Feature.SIZE, 20))
    modify_multiple_features(
        ax, Location.YLABEL, [(Feature.ALPHA, 0.5), (Feature.SLANT, "italic")]
    )

    fig.tight_layout()
    fig.show()
