from predict import predict
# from training import training
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


