"""The module contains the code that allows to change properties of the text
objects of the figure.
"""
from enum import Enum, auto


class Location(Enum):
    TITLE = auto()
    XLABEL = auto()
    YLABEL = auto()
    XTICKS = auto()
    YTICKS = auto()


class Feature(Enum):
    COLOR = "color"
    ALPHA = "alpha"
    SIZE = "size"
    FAMILY = "family"
    SLANT = "slant"


def modify_font(ax, location, feature_name, feature_value):
    """Change the text properties of the indicated graph element.

    Properties
    ----------
    ax : matplotlib.axes.Axes
        Object containing text to be modified
    location : Location
        For the list of supported features see Location definition.
    feature_name : Feature
        For the list of supported features see Feature definition.
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
    if location == Location.TITLE:
        my_texts = [ax.title]
    elif location == Location.XLABEL:
        my_texts = [ax.xaxis.label]
    elif location == Location.YLABEL:
        my_texts = [ax.yaxis.label]
    elif location == Location.XTICKS:
        my_texts = [tick.label for tick in ax.xaxis.majorTicks]
    elif location == Location.YTICKS:
        my_texts = [tick.label for tick in ax.yaxis.majorTicks]
    else:
        raise ValueError("Location not suported.")

    for text in my_texts:
        if feature_name in [Feature.COLOR, Feature.ALPHA]:
            setattr(text, f"_{feature_name.value}", feature_value)
        else:
            setattr(text._fontproperties, f"_{feature_name.value}", feature_value)

    return ax


def modify_multiple_elements(ax, locations="all", feature=(Feature.FAMILY, "serif")):
    """Modify multiple elements.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Object containing text to be modified
    locations : list(Location) or str, optional
        For the list of supported features see Location definition.
        By default all available locations are modified.
    feature : tuple, optional
        Tuple composed of Feature name and its value: (Feature.COLOR, "red").
        By default the font family is changed to serif.
    """
    if locations == "all":
        locations = [location for location in Location]
    for location in locations:
        modify_font(ax, location, feature[0], feature[1])
    return ax


def modify_multiple_features(ax, location, features):
    """Modify multiple features.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Object containing text to be modified
    location : Location
        For the list of supported features see Location definition.
        By default all available locations are modified.
    features : list(tuple)
        List of tuples composed of feature name and its value:
        [(Feature.COLOR, "red"), (Feature.FAMILY, "serif")].
    """
    for feature in features:
        modify_font(ax, location, feature[0], feature[1])
    return ax
