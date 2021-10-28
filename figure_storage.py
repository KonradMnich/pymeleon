import pickle
from datetime import datetime
import matplotlib.pyplot as plt


def store_figure(figure, path=None):
    """Saves figure to file for later usage.

    Parameters
    ----------
    figure : matplotlib.figure.Figure
        Figure to be stored.
    path : path-like, optional
        Path under which the figure should be saved.
    """
    if path is None:
        path = f"Figure_{datetime.utcnow()}"
    with open(path, "wb") as f:
        pickle.dump(figure, f)


def restore_visualization(fig):
    """Restore the capability to show the figure after
    it was closed or read from file.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to be treated.
    """
    dummy = plt.figure()
    new_manager = dummy.canvas.manager
    new_manager.canvas.figure = fig
    fig.set_canvas(new_manager.canvas)
    return fig


def read_figure(path, enable_show=True):
    """Read figure from file.

    Parameters
    ----------
    path : path-like
        Path to the figure.
    enable_show : bool, optional
        If set to false, the user won't be able to visualize the figure with
        the .show() syntax.
    """
    with open(path, "rb") as f:
        fig = pickle.load(f)

    if enable_show:
        fig = restore_visualization(fig)

    return fig
