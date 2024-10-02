from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import os
import numpy as np


# original thetas (global to be used in different functions)
t0 = 0.0
t1 = 0.0

def predict_data(x):
    return (t0 + (t1 * x))


def def_thetas(x, y):
    '''
    Parameters
    ----------
    l_rate : float
        Learning rate
    n_iter : int
        Number of passes over the training set
    
    mae = Mean Absolute Error > loss function (residus, marge d'erreur)
    Simple linear regression aims to represent the relationship between a feature and a target variable.
    doc : https://medium.com/@leogaudin/ft-linear-regression-an-introduction-guide-to-machine-learning-at-42-4d9a19a260e5

    to estimate the price for a mileage, subtract it (the mileage) to the actual price in the data we have,
    do this for all the data points, and then divide the sum by the number of data points.
    

    # docs :
    # linear regression, explication et calcul des thetas :
    # https://moncoachdata.com/blog/regression-lineaire-avec-python/
    '''
    
    # original thetas:
    global t0, t1

    # thetas before training:

    print('Thetas before training: {} {}'.format(t0, t1))

    # values to modify, just a simple point of departure
    l_rate = 0.5
    n_iter = 500

    # memory for graphics (t0, t1)
    m_t0 = []
    m_t1 = []

    # estimation of price for each mileage

    for j in range(n_iter):
        gradient_t0 = (sum([predict_data(x[i]) - y[i] for i in range(len(x))]) / len(x))
        gradient_t1 = (sum([(predict_data(x[i]) - y[i]) * x[i] for i in range(len(x))]) / len(x))

        t0 -= l_rate * gradient_t0
        t1 -= l_rate * gradient_t1
        m_t0.append(t0)
        m_t1.append(t1)

    print('Thetas after training (normalised data): {:.5} {:.5}'.format(t0, t1))

    # write thetas in a csv file
    # https://www.w3schools.com/python/ref_func_open.asp
    # https://www.w3schools.com/python/python_file_write.asp

    f = open('thetas.csv', 'w')
    f.write('{}, {}'.format(t0, t1))
    f.close()

    return(m_t0, m_t1)

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


def norm(data, x):
    min_x = min(data)
    mean = max(data) - min(data)
    return ((x - min_x) / mean)


def denorm(data, x):
    min_x = min(data)
    mean = max(data) - min_x
    res = min_x + (mean * x)
    return (res)


def print_graph(dataset, data, m_t0, m_t1):
    '''
    Print different graphs with data and evolution
    '''

    max_x = max(data[0])
    min_x = min(data[0])
    graph_x = sorted(data[0])

    # first graph : first prediction (data plot)
    
    plt.title('First prediction (data plot)')
    dataset.plot.scatter(x='km', y='price', marker='*')
    plt.plot([max_x, min_x], [min(data[1]), max(data[1])], 'o:r')  # 'o:r' = pointillés rouges

    plt.show()

    # 2nd graph : theta0 evolution

    plt.title('Theta0 evolution')
    plt.xlabel('iterations')
    plt.ylabel('theta0')
    plt.plot(m_t0)
    plt.show()

    # 3rd graph : theta1 evolution

    plt.title('Theta1 evolution')
    plt.xlabel('iterations')
    plt.ylabel('theta1')
    plt.plot(m_t1)
    plt.show()

    # 4th graph : final prediction compare to first one
    
    # graph_x = [float(min_x), float(max_x)]
    # y1 = t0 + ((norm(data[0], graph_x[0])) * t1)
    # y2 = t0 + ((norm(data[0], graph_x[1])) * t1)
    # graph_y = [denorm(data[1], y1), denorm(data[1], y2)]
    # dataset.plot.scatter(x='km', y='price', marker='*')
    # plt.plot([graph_x[0], graph_x[1]], [graph_y[0], graph_y[1]], 'r')
    # plt.title('Final prediction')
    
    y1 = []
    graph_y = []

    # graph_x = sorted(data[0])
    for i in range(len(data[0])):
        y1.append(t0 + ((norm(data[0], graph_x[i])) * t1))
    for i in range(len(data[1])):
        graph_y.append(denorm(data[1], y1[i]))
    dataset.plot.scatter(x='km', y='price', marker='*')
    plt.plot(graph_x, graph_y, 'r')
    plt.plot([max_x, min_x], [min(data[1]), max(data[1])], 'o:g')
    plt.title('Final prediction')
    
    plt.show()


def main():

    # Load data
    try:
        data_path = os.path.join(os.getcwd(), "data.csv")
        dataset = read_csv(data_path)
    except Exception:
        return print("ERROR : Unvalid path/file for data")


    data = read_csv("data.csv").to_numpy().transpose()  # data sous forme de matrice

    # normalized data 
    
    x = normalize(data[0])
    y = normalize(data[1])

    # finding thetas :
    m_t0, m_t1 = def_thetas(x, y)

    # print graphics:
    print_graph(dataset, data, m_t0, m_t1)


if __name__ == "__main__":
    main()


# Excellent readme, explications mathématiques et exemples :
# https://medium.com/@leogaudin/ft-linear-regression-an-introduction-guide-to-machine-learning-at-42-4d9a19a260e5
