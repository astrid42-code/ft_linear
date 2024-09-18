import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np
import os
from train import normalize


def normalize_price(user, data_x):
    '''
    normalize user mileage for 1st step

    return int (normalized mileage)
    '''

    min_x = min(data_x)
    mean = max(data_x) - min_x  # x data's mean
    return ((user - min_x) / mean)


def denormalize_price(norm_price, norm_data_x):
    # denormaliser le résultat:

    min_data = min(norm_data_x)
    mean_data = max(norm_data_x) - min_data
    res = min_data + (mean_data * norm_price)
    # print("data", norm_data_x, "norm" , norm_price)

    return(res)

def find_price(data, norm_data_x, thetas, user):
    '''
    solve formula : estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
    '''

    # normalized user data:
    res = normalize_price(user, data[0])
    # print(res)

    # prediction avec user data et thetas normés:
    norm_price = thetas[0] + (thetas[1] * res)

    # print("1", thetas[1] , "0", thetas[0])
    # print("norm", norm_price)
    # resultat de la prediction denormalisé (pour avoir le prix non normalisé)
    final_price = denormalize_price(norm_price, data[1])
    # print("final", final_price)
    return (final_price)



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

    final_price = find_price(data, norm_data_x, prediction, user)
    if final_price <= 0:
        print("This car is too old, you should throw it away!")
    else:
        print('You can sell it {} euros'.format(int(final_price)))


if __name__ == "__main__":
    main()