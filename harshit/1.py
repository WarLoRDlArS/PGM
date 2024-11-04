import random as rand

def dice_roll():
    s = [1, 2, 3, 4, 5, 6]
    x = rand.choice(s)
    return x

def probability(iteration, file):
    with open(file, "wt") as f:
        ones = 0
        sixes = 0
        for i in range(1, iteration+1):
            x = dice_roll()
            if x == 1:
                ones += 1 

            elif x == 6:
                sixes += 1

            if (i % (iteration / 10)) == 0:
                print(f"Iteration {i}\t Dice rolled {x}")
            if ones == 0 or sixes == 0:
                f.write(f"Iteration {i} :, ones={ones}, sixes={sixes}\n")
            else:
                f.write(f"Iteration {i} :, Ones : {float(ones) / i}, sixes={(float(sixes) / i)}\n")
        print(f"Proportion of Ones : {ones / iteration}")
        print(f"Propertion of Sixes : {sixes / iteration}")

def main():
    probability(1000, "test1.csv")
    probability(10000, "test2.csv")

if __name__ == "__main__":
    main()