from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import csv


def ft_thetas(data):
    t0 = 0
    t1 = 0
    with open(data, 'r') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        for row in data:
            t0 = float(row[0])
            t1 = float(row[1])
            print("t0 = ", t0)
            print("t1 = ", t1)
    return(t0, t1)

def prediction(thetas):
    '''Function that predicts the estimated price of a car for a given mileage.
    User has to enter a correct value for mileage (int only)
    Before the run of the training program,
    theta0 and theta1 will be set to 0'''


    # mileage = estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
    mileage = int(input("Enter the mileage of your car : "))
    # if isinstance(mileage, int) is False:
    #     return print("ValueError: invalid literal for int() with base 10")
        # > pb directement traite par python (car caste a l initialisation)
        # doit on handle error alors?
    
    print("The mileage is : ", mileage)





def main():
    # calculer les thetas 

    data = load("data.csv")
    if data is None:
        return print('Error in data')
    load pas reutilisable ici car on ne veut pas un dataframe en retour
    ou alors changer valeur de retour de la fct (expected str, nytes or os.PathLike object)
    # print(data)
    # data.plot(xlabel='Year', ylabel='km',
    #             title='Data')
    # plt.show()
    thetas = ft_thetas("data.csv")
    prediction(thetas)

if __name__ == "__main__":
    main()

# # cf https://www.toptal.com/machine-learning/supervised-machine-learning-algorithms
# # yi ≈ θ∗0 + θ∗xi
# # θ∗1 coefficient directeur
# # θ∗0 ordonnée à l’origine
# # [ici : yi = estimatePrice, xi = mileage]
# # https://lms.fun-mooc.fr/c4x/MinesTelecom/04006/asset/T%C3%A9l%C3%A9com_FBD_S5_Statistique_V4.pdf
