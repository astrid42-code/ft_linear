from pandas import read_csv
import matplotlib.pyplot as plt
import os
import numpy as np


def def_thetas(x, y):
    '''
        Parameters
    ----------
    l_rate : float
        Learning rate
    n_iter : int
        Number of passes over the training set

    # docs :
    # linear regression, explication et calcul des thetas :
    # https://moncoachdata.com/blog/regression-lineaire-avec-python/
    '''
    
    # values to modify, just a simple point of departure
    l_rate = 0.05
    n_iter = 1000

    for i in range(iterations):
            # y_pred = np.dot(x, self.w_)
            # residuals = y_pred - y
            # gradient_vector = np.dot(x.T, residuals)
            # self.w_ -= (self.eta / m) * gradient_vector
            # cost = np.sum((residuals ** 2)) / (2 * m)
            # self.cost_.append(cost)



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

    # original thetas:
    t0 = 0.0
    t1 = 0.0

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

    # print("x=", x, "y=", y)

    # finding thetas :
    def_thetas(x, y)



if __name__ == "__main__":
    main()

