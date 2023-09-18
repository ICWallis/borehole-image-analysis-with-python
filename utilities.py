
import numpy as np

def random_strikes(n, mean, std_dev, lower_bound=0, upper_bound=360):
    """
    Generate a list of n random strike angles with a normal distribution, limited to a specified range.

    Parameters:
    - n (int): The number of random strike angles to generate.
    - mean (float): The mean strike angle in degrees.
    - std_dev (float): The standard deviation of the strike angles in degrees.
    - lower_bound (float, optional): The lower bound for the generated strike angles (default: 0 degrees).
    - upper_bound (float, optional): The upper bound for the generated strike angles (default: 360 degrees).

    Returns:
    - List of random strike angles following a normal distribution within the specified range.
    
    Notes:
    - This function generates random strike angles with parameters mean and std_dev.
    - Strike angles are in degrees and may wrap around within the specified range.
    - Values outside the specified range [lower_bound, upper_bound] are adjusted to fall within the range.
    """
    
    # Rest of the function code...


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
    """
    Generate a list of n random dip angles with a normal distribution, limited to a specified range.

    Parameters:
    - n (int): The number of random dip angles to generate.
    - mean (float): The mean dip angle of the normal distribution.
    - std_dev (float): The standard deviation of the dip angles.
    - lower_bound (float, optional): The lower bound for the generated dip angles (default: 0 degrees).
    - upper_bound (float, optional): The upper bound for the generated dip angles (default: 90 degrees).

    Returns:
    - List of random dip angles following a normal distribution within the specified range.

    Notes:
    - This function generates random dip angles with parameters mean and std_dev.
    - Dip angles are in degrees and may wrap around within the specified range.
    - Values outside the specified range [lower_bound, upper_bound] are adjusted to fall within the range.
    """
    
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


def random_depths_normal(n, mean, std_dev, lower_bound, upper_bound, outlier_handling=4):
    """Generate a list of n random depths a normal distribution within a specified range.
    
    Parameters:
    - n (int): The number of random depths to generate.
    - mean (float): The mean depth of the normal distribution.
    - std_dev (float): The standard deviation of the normal distribution.
    - lower_bound (float): The lower bound for the generated depths.
    - upper_bound (float): The upper bound for the generated depths.
    - outlier_handling (int, optional): A factor used for handling values outside the range. 
      Default is 4, which moves values back into the desired depth range.

    Returns:
    - List of random depths following a normal distribution within the specified range."""
    
    random_depths = np.random.normal(mean, std_dev, n)

    depths = []
    for depth in random_depths:
        if depth < lower_bound:
            depths.append(depth + lower_bound/outlier_handling)
        elif depth > upper_bound:
            depths.append(depth - upper_bound/outlier_handling)
        else:
            depths.append(depth)

    return depths

def random_depths_uniform(n, lower_bound, upper_bound):
    """Generate a list of n random depths with a uniform distribution within a specified range.

    Parameters:
    - n (int): The number of random depths to generate.
    - lower_bound (float): The lower bound for the generated depths.
    - upper_bound (float): The upper bound for the generated depths.

    Returns:
    - List of random depths following a uniform distribution within the specified range.
    """

    random_depths = np.random.uniform(lower_bound, upper_bound, n)

    return random_depths

def random_aperture_lognormal(mean, std_dev, min_limit, max_limit, num_values):
    """
    Generate random lognormal values within a specified range.

    Parameters:
    - mean_ln: Mean of the underlying normal distribution.
    - std_dev_ln: Standard deviation of the underlying normal distribution.
    - min_limit: Minimum limit for the generated values.
    - max_limit: Maximum limit for the generated values.
    - num_values: Number of values to generate.

    Returns:
    - List of generated lognormal values within the specified range.

    Notes:
    - Values outside the specified range [min_limit, max_limit] are not sampled.
    """
    lognormal_values = []
    count = 0
    
    while count < num_values:
        value = np.random.lognormal(mean, std_dev)
        if min_limit <= value <= max_limit:
            lognormal_values.append(value)
            count += 1
    
    return lognormal_values