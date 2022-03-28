from const import *
import numpy as np
import pandas as pd

def damOperation(operationModel, inputFilePath, outputFilePath):
    data = pd.read_csv(inputFilePath)
    inflow = data[INFLOW_LABEL]
    timeSeries = data[TIME_LABEL]

    outflow, storage = operationModel(inflow)

    output = pd.DataFrame({
        TIME_LABEL: timeSeries,
        OUTFLOW_LABEL: outflow,
        STORAGE_LABEL: storage
    })

    output.to_csv(outputFilePath)


def model1(inflow):
    outflow = []
    storage = []
    currentStorage = 0

    TOTAL_TIME_STEP = len(inflow)
    MAX_OUTFLOW = 250

    for t in range(TOTAL_TIME_STEP):
        if inflow[t] < MAX_OUTFLOW:
            outflow.append(inflow[t])
        else:
            outflow.append(MAX_OUTFLOW)
            currentStorage += inflow[t] - MAX_OUTFLOW
        storage.append(currentStorage)

    return outflow, storage


def model2(inflow):
    outflow = []
    storage = []
    currentStorage = 0

    TOTAL_TIME_STEP = len(inflow)
    OUTFLOW_THR = 150
    COEFF = 0.4
    PEAK_OUTFLOW = 0
    isBeforePeak = True

    for t in range(TOTAL_TIME_STEP):
        if (0 < t and inflow[t-1] > inflow[t]):
            isBeforePeak = False
            PEAK_OUTFLOW = outflow[t-1]
        
        if inflow[t] < OUTFLOW_THR:
            outflow.append(inflow[t])
        elif isBeforePeak:
            outflow.append((inflow[t] - OUTFLOW_THR) * COEFF + OUTFLOW_THR)
            currentStorage += (inflow[t] - OUTFLOW_THR) * (1 - COEFF)
        elif PEAK_OUTFLOW < inflow[t]:
            outflow.append(PEAK_OUTFLOW)
            currentStorage += inflow[t] - PEAK_OUTFLOW
        else:
            outflow.append(inflow[t])

        storage.append(currentStorage)

    return outflow, storage



def main():
    damOperation(model1, INPUT_FILE_PATH, OUTPUT_FILE_PATH_MODEL1)
    damOperation(model2, INPUT_FILE_PATH, OUTPUT_FILE_PATH_MODEL2)


if __name__ == "__main__":
    main()
