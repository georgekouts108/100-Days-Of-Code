import random

games_played = 0

CARDS = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'AceHi':11, 'AceLo':1}

def hit(cards):
    
    _cards = cards
    next_card_face = random.choice(list(CARDS.keys())[:-1])
    _cards.append(next_card_face)
    
    updated_total = sum( [CARDS[face] for face in _cards] )

    
    if updated_total > 21:
        busted = True
        temp_total = updated_total
        for c in range(len(_cards)):
            if _cards[c] == 'AceHi':
                _cards[c] = 'AceLo'
                temp_total -= 10

            if temp_total <= 21:
                busted = False
                break

        return (_cards, busted, temp_total)

    return (_cards, False, updated_total)

def get_cpu_result(cards):
    _cards = cards
    busted = False
    cards_total = sum( [CARDS[face] for face in _cards] )

    while not busted and cards_total < 17:
        _cards, busted, cards_total = hit(_cards)

    return (_cards, busted, cards_total)
       

def play():

    # draw your first 2 cards
    first_card = random.choice(list(CARDS.keys())[:-1])
    second_card = random.choice(list(CARDS.keys())[:-1])

    your_cards = [first_card, second_card]
    if first_card==second_card and first_card=='AceHi':
        your_cards = ['AceHi', 'AceLo']
        
    # draw the cpu's first 2 cards
    cpu_hidden = random.choice(list(CARDS.keys())[:-1])
    cpu_first_card = random.choice(list(CARDS.keys())[:-1])

    cpu_cards = [cpu_hidden, cpu_first_card]
    if cpu_first_card==cpu_hidden and cpu_first_card=='AceHi':
        cpu_cards = ['AceHi', 'AceLo']
    
    print(f"Your cards: {your_cards}")
    print(f"CPU's first card: {cpu_first_card} {'('+str(CARDS[cpu_first_card])+')' if cpu_first_card in ['Jack','Queen','King','Ace'] else ''}")

    # did cpu get blackjack?
    cpu_got_blackjack = ((cpu_first_card=='AceHi' and cpu_hidden in ['10','Jack','Queen','King'])
                     or (cpu_hidden=='AceHi' and cpu_first_card in ['10','Jack','Queen','King']))

    if cpu_got_blackjack:
        print("CPU got blackjack! You lose!")
        return

    # did you get blackjack?
    you_got_blackjack = ((first_card=='AceHi' and second_card in ['10','Jack','Queen','King'])
                     or (second_card=='AceHi' and first_card in ['10','Jack','Queen','King']))

    if you_got_blackjack:
        print("Congrats! You got blackjack!")
        
    else:
        busted = False
        cards_total = CARDS[first_card] + CARDS[second_card]
        while not busted:
            print(f"Your cards = {your_cards} -- total = {cards_total}")

            if cards_total == 21:
                print("You got 21!\n")
                break

            if input("\nType \'y\' to get another card (hit) or \'n\' to stand: ") == 'n':
                break
           
            your_cards, busted, cards_total = hit(your_cards)

            
        
        if busted:
            print(f"Your final cards: {your_cards}")
            print(f"CPU's final cards: {cpu_cards}")
            print(f"Sorry, you busted with a total of {cards_total}!")
        else:
            cpu_cards, cpu_busted, cpu_total = get_cpu_result(cpu_cards)

            if cpu_busted:
                print(f"Your final cards: {your_cards}")
                print(f"CPU's final cards: {cpu_cards}")
                print(f"The CPU busted with {cpu_total}! You win!")
            else:
                print(f"Your final cards: {your_cards}")
                print(f"CPU's final cards: {cpu_cards}")
                if cards_total == cpu_total:
                    print(f"It's a push! YOU {cards_total} - {cpu_total} CPU")
                elif cards_total > cpu_total:
                    print(f"You win! YOU {cards_total} - {cpu_total} CPU")
                elif cards_total < cpu_total:
                    print(f"You lose! YOU {cards_total} - {cpu_total} CPU")     


while True:
    play_decision = input(f"\n\nDo you want to play a{'nother' if games_played>0 else ''} game of Blackjack? Type \'y\' or \'n\': ")
    
    if play_decision == 'n':
        break
    else:
        games_played += 1
        print("\n")
        play()
        
        
        
