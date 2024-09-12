from pandas import read_csv
import matplotlib.pyplot as plt
import os
import numpy as np

def main():
    # values to modify, just a simple point of departure
    # learning_rate = 0.1
    # iterations = 100

    # Load data
    try:
        data_path = os.path.join(os.getcwd(), "data.csv")
        # print(data_path)
        # dataset = read_csv(data_path, index_col=0)  # delim_whitespace=True)
        dataset = read_csv(data_path)
    except Exception:
        return print("ERROR : Unvalid path/file")
    # print(dataset)

    dataset.plot.scatter(x='km', y='price')
    plt.show()

    data = read_csv("data.csv").to_numpy()  # data sous forme de matrice
    print(data)


if __name__ == "__main__":
    main()