from pandas import read_csv
import matplotlib.pyplot as plt
import os
import numpy as np

# original thetas (global to be used in different functions)
t0 = 0.0
t1 = 0.0

def predict_data(x):
    # print(t0 + (t1 * x))
    return (t0 + (t1 * x))

def mae(x, y):
    '''
    mae = Mean Absolute Error > loss function (residus, marge d'erreur)
    Simple linear regression aims to represent the relationship between a feature and a target variable.
    doc : https://medium.com/@leogaudin/ft-linear-regression-an-introduction-guide-to-machine-learning-at-42-4d9a19a260e5

    to estimate the price for a mileage, subtract it (the mileage) to the actual price in the data we have,
    do this for all the data points, and then divide the sum by the number of data points.
    '''
    
    mae = 0
    for i in range(len(x)):
        # print(x[i] - predict_data(x[i]))
        mae += abs(predict_data(x[i]) - y[i])
    mae /= len(x)
    print(mae)


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
    
    # original thetas:
    global t0, t1

    # values to modify, just a simple point of departure
    l_rate = 0.05
    n_iter = 1000

    # estimation of price for each mileage

    for j in range(n_iter):
        gradient_t0 = (sum([predict_data(x[i]) - y[i] for i in range(len(x))]) / len(x))
        gradient_t1 = (sum([(predict_data(x[i]) - y[i]) * x[i] for i in range(len(x))]) / len(x))
        # print("xi", x[i], "predict_x", predict_data(x[i]), "yi", y[i])
        # print("tmp0 ", gradient_t0, len(x))

        t0 -= l_rate * gradient_t0
        t1 -= l_rate * gradient_t1
    print("t0", t0, "t1", t1)

    # mae(x)


        



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
    mean = max(data) - min_data  # data's mean
    res = []
    for i in data:
        res.append((i - min_data) / mean)
    return(np.array(res))


def main():


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

    # finding thetas :
    def_thetas(x, y)



if __name__ == "__main__":
    main()


# Excellent readme, explications mathématiques et exemples :
# https://medium.com/@leogaudin/ft-linear-regression-an-introduction-guide-to-machine-learning-at-42-4d9a19a260e5
