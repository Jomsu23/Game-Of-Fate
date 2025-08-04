 ##### Functions #####

def check_factor(list, number):
    # Check if the card picked has at least one factor still on the table
    for n in list :
        if n < number and number%n == 0 :
            return 1
        continue
    return 0

def check_availability(list, number):
    # Check if the card picked is still in the deck
    return(number in list)
        
def update_score(new_score):
    with open('scores.txt', 'w') as f:
            f.write(new_score)

def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = int(lines[0].strip())

    return score

##### Set up #####

high_score = max_score()

deck = [n for n in range (1,24)]
players_hand = []
fates_hand = []

game_over = 0

print("The game begins \n Here are the cards :\n ", deck)

##### Game #####

while game_over != 1 :

    # Player choose a card
    try:
        pick = int(input("Choose a card : \n"))
    except ValueError:
        print("\n This is not a valid pick. Enter a number from 1 to 23 \n")
        continue

    if check_availability(deck, pick) == 0 :
        print("This card is no longer available")
        continue

    if check_factor(deck, pick) == 0 :
        print(" You can only take numbers that have at least one factor on the table.")
        continue

    # Update player's hand
    players_hand.append(pick)
    # Update deck
    deck.remove(pick)

    # Update Fate's hand
    for card in deck :
        if pick % card == 0 :
            fates_hand.append(card)

    # Update deck
    for card in fates_hand :
        if card in deck :
            deck.remove(card)

    print("Your cards : \n", players_hand, "    It adds to ", sum(players_hand), "\n")
    print("Fate's cards : \n", fates_hand, "    It adds to ", sum(fates_hand), "\n")
    print("Cards still in play : \n", deck, "\n")

    # Is game still playable ?
    if all(check_factor(deck, card) == 0 for card in deck) == 1 :
        game_over = 1
        print("You can't pick any other card. The game is over")

# The game has ended

# Update Fate's hand
fates_hand = fates_hand + deck
deck = []

# Final score
print("Your cards : \n", players_hand, "    It adds to ", sum(players_hand), "\n")
print("Fate's cards : \n", fates_hand, "    It adds to ", sum(fates_hand), "\n")

if sum(players_hand) > sum(fates_hand) :
    print("Congratulations ! You've won. \n")
    if sum(players_hand) > high_score :
        print("\n You've beat the precedent best ", high_score)
        update_score(str(sum(players_hand)))

    if 2 in players_hand :
        print("And you broke the curse. \n ")
    elif 6 in players_hand :
        print("And you'll soon meet your True Love. \n")
    elif 10 in players_hand :
        print("And you'll receive unimaginable riches. \n")
    else :
        print("Sadly you gained no additionnal rewards. \n")
else :
    print("Oh no, you've lost... Fate will claim your soul :( \n")