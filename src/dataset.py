import pandas as pd
import numpy as np

heights = [1.8, 1.75, 1.6, 1.9, 1.85]
weights = [70, 80, 60, 90, 75]
heroes = ["Superman", "Batman", "Wonder"]


def convert_units(heroes, heights, weights):
    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}
    # Create a dictionary from the heroes, heights, and weights
    for i, hero in enumerate(heroes):
        hero_data[hero] = (heights[i], weights[i])

    # Update the heights and weights in the dictionary
    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data


# pip install line_profiler
# %load_ext line_profiler
# %lprun -f convert_units convert_units(heroes, hts, wts)


############################ Using Array Broadcasting ############################
def convert_units_broadcast(heroes, heights, weights):
    # Convert to numpy arrays
    heights = np.array(heights)
    weights = np.array(weights)

    # Convert units using broadcasting
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    # Create a DataFrame from the heroes, heights, and weights
    hero_data = pd.DataFrame({"Hero": heroes, "Height": new_hts, "Weight": new_wts})

    return hero_data
