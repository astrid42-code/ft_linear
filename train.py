# https://www.toptal.com/machine-learning/supervised-machine-learning-algorithms

from pandas import read_csv
# import pandas as pd
import matplotlib.pyplot as plt
import os



def main():
    # values to modify, just a simple point of departure
    hypothesis = 5000
    rate = 1
    # Load data

    try:
        data_path = os.path.join(os.getcwd(), "data.csv")
        # dataset = read_csv(data_path, index_col=0) # , delim_whitespace=True
        dataset = read_csv(data_path)
    except Exception:
        return print("Unvalid path/file")

    # print(dataset)

    # plt.plot(dataset)



# # We have 30 entries in our dataset and four features. The first feature is the ID of the entry.
# # The second feature is always 1. The third feature is the age and the last feature is the blood pressure.
# # We will now drop the ID and One feature for now, as this is not important.
# dataset = dataset.drop(['ID', 'One'], axis=1)

# # And we will display this graph
# %matplotlib inline
    # dataset.plot.scatter(x='km', y='price')

# # Now, we will assume that we already know the hypothesis and it looks like a straight line
    # cost function (which calculates the root mean square error between the model prediction and the actual output)

    # ex : 
    # h = lambda x: 84 + 1.24 * x
    h = lambda x: hypothesis + rate * x

# # Let's add this line on the chart now
# ages = range(18, 85)
    kms = range(50000, 250000)
    estimated = []

    for i in kms:
        estimated.append(h(i))

    plt.plot(kms, estimated, 'b')  
    plt.show()


if __name__ == "__main__":
    main()