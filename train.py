# https://www.toptal.com/machine-learning/supervised-machine-learning-algorithms

from pandas import read_csv
# import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# def cost_fct()

def load_data():
    try:
        data_path = os.path.join(os.getcwd(), "data.csv")
        dataset = read_csv(data_path)
    except Exception:
        return print("Unvalid path/file")

    print(dataset)

    dataset.plot.scatter(x='km', y='price')
    plt.show()

    mileage = []
    prices = []
    for i in dataset:
        mileage.append(i[0])
        prices.append(i[1])
        print(mileage, prices)


def main():
    # values to modify, just a simple point of departure
    learning_rate = 0.1
    iterations = 100

    # Load data
    load_data()

    data = read_csv("data.csv").to_numpy()  # data sous forme de matrice
    print(data)


# We have 30 entries in our dataset and four features. The first feature is the ID of the entry.
# The second feature is always 1. The third feature is the age and the last feature is the blood pressure.
# We will now drop the ID and One feature for now, as this is not important.
# dataset = dataset.drop(['ID', 'One'], axis=1)

# # And we will display this graph
# %matplotlib inline
    # dataset.plot.scatter(x='km', y='price')
    # plt.show()

# # Now, we will assume that we already know the hypothesis and it looks like a straight line
    # cost function (which calculates the root mean square error between the model prediction and the actual output)

    # ex : 
    # h = lambda x: 84 + 1.24 * x
    # h = lambda x: hypothesis + rate * x

# # Let's add this line on the chart now
# ages = range(18, 85)
    # kms = range(50000, 250000)
    # estimated = []

    # for i in kms:
    #     estimated.append(h(i))
    # print(estimated)

    # plt.plot(kms, estimated, 'y')


if __name__ == "__main__":
    main()