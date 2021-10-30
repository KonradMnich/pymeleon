"""Change font properties of the elements of axis."""
from pymeleon.font_modifiers import modify_font
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fig, ax = plt.subplots()

    ax.plot([0, 1], [0, 1])
    modify_font(ax, "xticks", {"name": "size", "value": 20})
    modify_font(ax, "xticks", {"name": "family", "value": "serif"})
    modify_font(ax, "xticks", {"name": "slant", "value": "italic"})
    ax.set_ylabel("my text")
    modify_font(ax, "ylabel", {"name": "family", "value": "fantasy"})
    modify_font(ax, "ylabel", {"name": "size", "value": 25})
    fig.show()
