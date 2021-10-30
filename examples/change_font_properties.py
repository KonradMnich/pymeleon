"""Change font properties of the elements of axis."""
from pymeleon.font_modifiers import modify_font
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fig, ax = plt.subplots()

    ax.plot([0, 1], [0, 1])
    modify_font(ax, "xticks", "size", 20)
    modify_font(ax, "xticks", "family", "serif")
    modify_font(ax, "xticks", "slant", "italic")
    ax.set_ylabel("my text")
    modify_font(ax, "ylabel", "family", "fantasy")
    modify_font(ax, "ylabel", "size", 25)
    fig.show()
