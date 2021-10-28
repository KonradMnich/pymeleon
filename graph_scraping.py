"""The module is designed to get numerical data from matplotlib figures."""
import pandas as pd


def scrap_data(fig):
    """Get numerical data from matplotlib figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to get data from.

    Returns
    -------
    df : pandas.DataFrame
        Table with hierarchical column index representing x and y coordinates
        of each line from each axis of the figure.
    """
    all_data = []
    axes_data = []
    axes = fig.get_axes()
    for a, ax in enumerate(axes):
        lines = ax.get_lines()
        for line in lines:
            axes_data.append(pd.DataFrame(line.get_xydata(), columns=["x", "y"]))
        all_data.append(
            pd.concat(
                axes_data,
                axis=1,
                keys=[f"line{i}" for i in range(len(lines))]
            )
        )
        axes_data = []
    df = pd.concat(
        all_data,
        axis=1,
        keys=[f"axis{i}" for i in range(len(axes))]
    )
    return df
