from prediction import prediction
# from training import training
from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


# ouverture du .csv (penser a faire protections cf M02)
# sans colonne index > pour le programme de training
data = load("data.csv")
# print(data)
data.plot(xlabel='Year', ylabel='km',
             title='Data')
# plt.show()
prediction(data)


# Attention : comme ce sont deux programmes a lancer
# > penser a faire main dans chacun 
# > et a faire un tester pour l'evaluation