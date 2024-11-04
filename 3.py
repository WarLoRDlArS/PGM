def main():
    total = 0
    P = []
    X = [] 
    
    X = list(map(float, input("Enter Values of X: ").split()))
    P = list(map(float, input("Enter Values of P(X=x): ").split()))

    if sum(P) != 1.0:
        print("Probability Values exceed or does not sum up to 1.0!!")
        return
    
    # Calculate E[x] for each value of x
    EX = [P[i] * X[i] for i in range(len(X))]
    # Calculate E[x]**2 for each value of x
    EX2 = [P[i] * pow(X[i], 2) for i in range(len(X))]

    print(f"Expectation is : {sum(EX)}")

    # Calculate Variance: Variance = E[x^2] - (E[x])**2
    variance = sum(EX2) - pow(sum(EX), 2)
    print(f"Variance is {variance}")

if __name__ == "__main__":
    main()