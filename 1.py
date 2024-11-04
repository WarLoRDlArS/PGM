import random as rand

def select_card():
    """Select a Card from the Deck of 52 Cards(No Jokers included)."""
    colors = ['red', 'black']
    card_types_all = [['clubs', 'spades'], ['diamonds', 'hearts']] 
    card_color = rand.choice(colors)

    card_type = None
    if card_color == 'black':
        card_type = rand.choice(card_types_all[0])
    else:
        card_type = rand.choice(card_types_all[1])

    card_number = None
    card = ['King', 'Queen', "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace"]

    return card_color, card_type, rand.choice(card)


def simulate_card_draw(iterations = 100):
    """Simulate the drawing of a random card for the given iterations."""

    # count of the number of cards
    no_of_black = 0
    no_of_red = 0 

    for i in range(1, iterations + 1):
        color, card_type, card = select_card()
        if color == 'red': 
            no_of_red += 1
        else:
            no_of_black += 1
        if (i % (iterations / 10)) == 0:
            print(f"Iteration: {i} \t {color} Card Selected : {card_type}, {card}")
    
    print(f"Proportion of Red Cards: {no_of_red / iterations}\nProportion of Black Cards: {no_of_black / iterations}")
    
    print(f"\nThe Ratio of Black to Red Cards is {no_of_black / no_of_red}\n")

def main():
    simulate_card_draw(10)
    simulate_card_draw(1000)
    simulate_card_draw(10000)
    simulate_card_draw(100000)

if __name__ == "__main__":
    main()