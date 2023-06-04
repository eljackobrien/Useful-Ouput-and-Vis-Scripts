# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:07:04 2022

@author: Stackoverflow_user_importanceofbeingernest
"""
# =============================================================================
# Code taken from stackoverflow question 30079590
# Written by user ImportanceOfBeingErnest
# =============================================================================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

def get_cycle(cmap, N=None, use_index="auto"):
    """
    To set the cycler to a particular map and then revert, use:

        original_cycle = plt.rcParams["axes.prop_cycle"]

        plt.rcParams["axes.prop_cycle"] = get_cycle("cmap", num_colours)

        #~~~ plotting ~~~

        plt.rcParams["axes.prop_cycle"] = original_cycle

    """

    if isinstance(cmap, str):
        if use_index == "auto":
            if cmap in ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c']:
                use_index=True
            else:
                use_index=False
        cmap = matplotlib.cm.get_cmap(cmap)
    if not N:
        N = cmap.N
    if use_index=="auto":
        if cmap.N > 100:
            use_index=False
        elif isinstance(cmap, LinearSegmentedColormap):
            use_index=False
        elif isinstance(cmap, ListedColormap):
            use_index=True
    if use_index:
        ind = np.arange(int(N)) % cmap.N
        return plt.cycler("color",cmap(ind))
    else:
        colors = cmap(np.linspace(0,1,N))
        return plt.cycler("color",colors)

