
import numpy as np

def random_strikes(n, mean, std_dev, lower_bound=0, upper_bound=360):
    """Returns a list of n random integers with a normal distribution 
    that has a default limited to 0 to 360."""

    random_strikes = np.random.normal(mean, std_dev, n)
    
    strikes = []
    for strike in random_strikes:
        if strike < lower_bound:
            strikes.append(strike + 180)
        elif strike > upper_bound:
            strikes.append(strike - 180)
        else:
            strikes.append(strike)

    return strikes

def random_dips(n, mean, std_dev, lower_bound=0, upper_bound=90):
    """Returns a list of n random integers with a normal distribution
    that has a default limited to 0 to 90."""
    
    random_dips = np.random.normal(mean, std_dev, n)

    dips = []
    for dip in random_dips:
        if dip < lower_bound:
            dips.append(dip + 45)
        elif dip > upper_bound:
            dips.append(dip - 45)
        else:
            dips.append(dip)

    return dips

def random_depths(n, mean, std_dev, lower_bound, upper_bound):
    """Returns a list of n random integers with a normal distribution
    that is limited to the upper and lower bound."""
    
    random_depths = np.random.normal(mean, std_dev, n)

    depths = []
    for depth in random_depths:
        if depth < lower_bound:
            depths.append(depth + lower_bound/2)
        elif depth > upper_bound:
            depths.append(depth - upper_bound/2)
        else:
            depths.append(depth)

    return depths
