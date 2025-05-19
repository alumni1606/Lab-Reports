import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def CI(B,V):
    # calculate nromalization factors
    normal_v = 1.888 * 10 ** (-18)
    normal_B = 8.797 * 10 ** (-18)

    #calculate the magnitude 
    mB = -2.5 * np.log10(B / normal_B)
    mV = -2.5 * np.log10(V / normal_v)
    # calculate the color index
    CI = mB - mV

    return  CI

def plot_color_index(data):
    # Create a scatter plot of the color index
    plt.figure(figsize=(10, 6))
    plt.scatter(data['B'], data['V'], c=data['CI'], cmap='viridis', s=10)
    plt.colorbar(label='Color Index (B-V)')
    plt.xlabel('B Magnitude')
    plt.ylabel('V Magnitude')
    plt.title('Color Index (B-V) Scatter Plot')
    plt.grid()
    plt.show()

B = 5.184 * 10 ** (-17)
V = 1.177 * 10 ** (-17)


print(CI(B,V))