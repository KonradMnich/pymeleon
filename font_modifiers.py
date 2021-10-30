"""The module contains the code that allows to change properties of the text
objects of the figure.
"""


def modify_font(ax, location, feature):
    """Change the text properties of the indicated graph element.

    Properties
    ----------
    ax : matplotlib.axes.Axes
        Object containing text to be modified
    location : str
        One of the following ["title", "xlabel", "ylabel", "xticks", "yticks",
        legend"]
    feature : dict
        Tells the function which feature to modify and how; ex:
        {"name": "color", "value": "red"}.
        List of supported properties: ["color", "alpha", "size", "family",
        "slant"] (but you can figure out what else is possible by looking at
        the source code.

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
        if feature["name"] in ["color", "alpha"]:
            setattr(text, f"_{feature['name']}", feature['value'])
        else:
            setattr(text._fontproperties, f"_{feature['name']}", feature['value'])

    return ax
