"""The module contains the code that allows to change properties of the text
objects of the figure.
"""


def modify_font(ax, location, feature_name, feature_value):
    """Change the text properties of the indicated graph element.

    Properties
    ----------
    ax : matplotlib.axes.Axes
        Object containing text to be modified
    location : str
        One of the following ["title", "xlabel", "ylabel", "xticks", "yticks",
        legend"]
    feature_name : str
        Supported features: "color", "alpha", "size", "family", "slant"
    feature_value : str or float
        New value for the changed feature

    Returns
    -------
    ax : matplotlib.axes.Axes
        Object containing the modified text.

    Notes
    -----
    For the list of available text features check out Matplotlib documentation:
    https://matplotlib.org/stable/tutorials/text/text_props.html (2021-10-30)
    """
    if location == "title":
        my_texts = [ax.title]
    elif location == "xlabel":
        my_texts = [ax.xaxis.label]
    elif location == "ylabel":
        my_texts = [ax.yaxis.label]
    elif location == "xticks":
        my_texts = [tick.label for tick in ax.xaxis.majorTicks]
    elif location == "yticks":
        my_texts = [tick.label for tick in ax.yaxis.majorTicks]
    else:
        raise ValueError("Location not suported.")

    for text in my_texts:
        if feature_name in ["color", "alpha"]:
            setattr(text, f"_{feature_name}", feature_value)
        else:
            setattr(text._fontproperties, f"_{feature_name}", feature_value)

    return ax
