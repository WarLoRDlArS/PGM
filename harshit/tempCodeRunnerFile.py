import random as rand  


def create_customer_data(iterations):
    with open("customer.csv", "wt") as f:
        for i in range(1, iterations + 1):
            customerID = rand.randrange(0, iterations)
            product_views = rand.randrange(1, 10)
            purchased = rand.choice([0, 1])

            f.write(f"{customerID}, {product_views}, {purchased}\n")


def main():
    create_customer_data(100)

    custId, views, purchased = [], [], []
    with open("customer.csv", "rt") as f:
        while True:
            data = f.readline()
            if data == "":
                break              
            x, y, z = list(map(int, data.split(", ")))
            custId.append(x)
            views.append(y)
            purchased.append(z)
    
    count1 = 0
    count2 = 0
    for i in range(len(custId)):
        if views[i] > 5 and purchased[i] == 1:
            count1 += 1
        if views[i] > 5:
            count2 += 1 

    print(f"Probability of product purchased given views greater than 5 is {float(count1) / count2}")
        


if __name__ == "__main__":
    main()