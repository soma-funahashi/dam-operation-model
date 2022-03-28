import sys
from turtle import color
sys.path.append('..')
from src.const import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from matplotlib import rc
rc('mathtext', default='regular')

def main():
    sns.set()
    sns.set_style("whitegrid", {'grid.linestyle': '--'})

    input = pd.read_csv(INPUT_FILE_PATH)
    output1 = pd.read_csv(OUTPUT_FILE_PATH_MODEL1)
    output2 = pd.read_csv(OUTPUT_FILE_PATH_MODEL2)

    inflow = input[INFLOW_LABEL]
    outflow1 = output1[OUTFLOW_LABEL]
    outflow2 = output2[OUTFLOW_LABEL]
    storage1 = output1[STORAGE_LABEL]
    storage2 = output2[STORAGE_LABEL]

    timeSeries = pd.to_datetime(input[TIME_LABEL])

    fig, ax1 = plt.subplots(figsize=(8,6))

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax2 = ax1.twinx()

    ax1.set_title("dam operation")
    ax1.set_xlabel("time")
    ax1.set_ylabel(r"inflow/outflow ($m^3/s$)")
    ax2.set_ylabel(r"dam storage ($m^3$)")

    inf = ax1.plot(timeSeries, inflow, label="inflow", color="black", lw=1.5)
    otf1 = ax1.plot(timeSeries, outflow1, label="outflow1", color="orange", lw=1.5)
    otf2 = ax1.plot(timeSeries, outflow2, label="outflow2", color="skyblue", lw=1.5)

    sto1 = ax2.plot(timeSeries, storage1, label="storage1", color="orange", ls='dotted', lw=1.5)
    sto2 = ax2.plot(timeSeries, storage2, label="storage2", color="skyblue", ls='dotted', lw=1.5)

    lines = inf + otf1 + otf2 + sto1 + sto2
    labs = [l.get_label() for l in lines]
    ax1.legend(lines, labs, loc="upper left")

    plt.savefig(FIGURE_PATH)

if __name__ == "__main__":
    main()
