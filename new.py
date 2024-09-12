from pandas import read_csv
import matplotlib.pyplot as plt
import os
import numpy as np


def normalize(data):
    '''
    La normalisation standard, également appelée standardisation ou normalisation z-score, consiste à soustraire la moyenne
    et à la diviser par l'écart type.
    Dans ce cas, chaque valeur refléterait la distance par rapport à la moyenne en unités d'écart-type.
    L'objectif de la normalisation est de modifier les valeurs des colonnes numériques du jeu de données
    pour utiliser une échelle commune, sans que les différences de plages de valeurs ne soient faussées et sans perte d'informations.
    
    docs : https://mrmint.fr/data-preprocessing-feature-scaling-python > normalisation
    formula : [X_{normalise} = \frac{X - X_{min}}{X_{max} - X_{min}}\]

    https://www150.statcan.gc.ca/n1/edu/power-pouvoir/ch12/5214891-fra.htm > ecart-type, variance

    '''
    
    min_data = min(data)
    diff_max_min = max(data) - min_data
    res = []
    for i in data:
        res.append((i - min_data) / diff_max_min)
    return(res)


def main():
    # values to modify, just a simple point of departure
    learning_rate = 0.1
    iterations = 100

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

    data = read_csv("data.csv").to_numpy().transpose()  # data sous forme de matrice
    print(data)

    # normalized data 
    
    
    x = normalize(data[0])
    y = normalize(data[1])

    print("x=", x, "y=", y)

    # hypothesis:
    # h = lambda x: iterations + learning_rate * x

    # kms = range(50000, 250000)
    # estimated = []

    # for i in kms:
    #     estimated.append(h(i))
    # print(estimated)


if __name__ == "__main__":
    main()