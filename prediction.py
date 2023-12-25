def prediction(data):
    '''Function that predicts the estimated price of a car for a given mileage.
    User has to enter a correct value for mileage (int only)
    Before the run of the training program,
    theta0 and theta1 will be set to 0'''


    if data is None:
        return print('Error in data')
    
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
    # print(data)
    # data.plot(xlabel='Year', ylabel='km',
    #             title='Data')
    # plt.show()
    prediction(data)

if __name__ == "__main__":
    main()

# cf https://www.toptal.com/machine-learning/supervised-machine-learning-algorithms
