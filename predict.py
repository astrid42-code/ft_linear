import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np
import os
from train import denormalize, normalize


def normalize_price(user, data_x):
    '''
    normalize user mileage for 1st step

    return int (normalized mileage)
    '''

    min_x = min(data_x)
    mean = max(data_x) - min_x  # x data's mean
    print("min", min_x, "mean", mean)
    return ((user - min_x) / mean)

def find_price(data, norm_data_x, prediction, user):
    '''
    solve formula : estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
    '''

    # normalized user data:
    res = normalize_price(user, data[0])
    print(res)

    # prediction avec user data et thetas normés:
    norm_price = prediction[0] + (prediction[1] * res)


    print("norm", norm_price)
    # resultat de la prediction denormalisé (pour avoir le prix non normalisé)
    final_price = denormalize(data[0], norm_price)
    print("final", final_price)
    return(final_price)



def main():

    # thetas storage 
    try:
        data_path = os.path.join(os.getcwd(), "thetas.csv")
        prediction = read_csv(data_path, header= None).to_numpy()[0]
    except Exception:
        return print("ERROR : Unvalid path/file for thetas")
    
    # print(prediction)
    
    print("Hello, please enter the mileage of your vehicule:")
    
    # user enters the mileage 
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

    # opening original data:
    try:
        data_path = os.path.join(os.getcwd(), "data.csv")
        data = read_csv(data_path).to_numpy().transpose()
    except Exception:
        return print("ERROR : Unvalid path/file for data")


    norm_data_x = normalize(data[0])
    norm_data_y = normalize(data[1])

    find_price(data, norm_data_x, prediction, user)


if __name__ == "__main__":
    main()