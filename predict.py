import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np
import os


def main():
    try:
        data_path = os.path.join(os.getcwd(), "thetas.csv")
        prediction = read_csv(data_path, header= None).to_numpy()[0]
    except Exception:
        return print("ERROR : Unvalid path/file for thetas")
    # print(prediction)
    
    print("Hello, please enter the mileage of your vehicule:")
    
    while (1):
        try:
            user = int(input(">> "))
        except Exception:
            return print("ERROR :  you must enter one number, int only. Please reload")
        
        if user > 0:
            break
        else:
            return print("ERROR :  you must enter a positive number (more than zero). Please reload")
            exit()


    try:
        data_path = os.path.join(os.getcwd(), "data.csv")
        data = read_csv(data_path).to_numpy().transpose()
    except Exception:
        return print("ERROR : Unvalid path/file for data")

    mileages = []
    prices = []
    for i in data[0]:
        mileages.append(i)
    for j in data[1]:
        prices.append(j)
    # print("m ", mileages, "p ", prices)

    

if __name__ == "__main__":
    main()