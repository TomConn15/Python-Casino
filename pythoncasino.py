import os
import random
# I ran my progtamon my mac usig the terminal.

# Function that deals with number bets in roulette.       
def number_pick(cash):
    number = random.randint(1,36)
    numList = list(int(num) for num in input("Enter the numbers(1-36) you want to bet on separated by a space:  ").strip().split())
    n = len(numList)
    try: 
        bet = int(input("How much would you like to bet on each number?  $"))
        totalbet = bet * n
        if totalbet > cash:
            print("You do not have enough money in the bank!")
            number_pick(cash) 
        if totalbet  <= cash:
            if number in numList:
                print("The winning number:",number,"\n Congratulations, you win!\n")
                cash = cash - totalbet + (36 * bet)
                print("Your new total is :  $", cash)
                play_again(cash)
            else:
                print("The winning number:",number,"\n Sorry, you lose.\n")
                cash = cash - totalbet
                print("Your new total is :  $", cash)
                play_again(cash)
    except ValueError:
        print("Invalid Input.")
        print("Please bet with whole dollars, we do not accept change!\n")
        number_pick(cash)

# Function that deals with deciding whether a number is even or odd in roulette.            
def even_odd(cash):
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    number = random.randint(1,36)
    try:
        bet = int(input("How much would you like to bet?  $"))
        if bet > cash:
            print("You do not have enough money in the bank!")
            even_odd(cash)
        if bet <= cash:
            pick = input("Choose: (O)dd or (E)ven.  ").lower()
            if pick == 'o':
                if number in odd:
                    print("The winning number:", number,"\n Congratulations, you win!\n")
                    cash = cash + bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
                if number in even:
                    print("The winning number:", number,"\n Sorry, you lose!\n")
                    cash = cash - bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
            if pick == 'e':
                if number in even:
                    print("The winning number:", number,"\n Congratulations, you win!\n")
                    cash = cash + bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
                if number in odd:
                    print("The winning number:", number,"\n Sorry, you lose!\n")
                    cash = cash - bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
            else:
                print("Invalid Input. Try again!")
                even_odd(cash)
    except ValueError:
        print("Invalid Input.")
        print("Please bet with whole dollars, we do not accept change!\n")
        even_odd(cash)
    
# Function that deals with deciding whether a number is red or black in roulette.       
def red_black(cash):
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    number = random.randint(1,36)
    try:
        bet = int(input("How much would you like to bet?  $"))
        if bet > cash:
            print("You do not have enough money in the bank!")
            red_black(cash)
        if bet <= cash:        
            pick = input("Choose: (R)ed or (B)lack.  ").lower()
            if pick == 'r':
                if number in red:
                    print("The winning number:", number,", is red.\n Congratulations, you win!\n")
                    cash = cash + bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
                if number in black:
                    print("The winning number:", number,", is black.\n Sorry, you lose.\n")
                    cash = cash - bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
            if pick == 'b':
                if number in black:
                    print("The winning number:", number,", is black.\n Congratulations, you win!\n")
                    cash = cash + bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
                if number in red:
                    print("The winning number:", number,", is red.\n Sorry, you lose.\n")
                    cash = cash - bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
            else:
                print("Invalid Input. Try again!")
                red_black(cash)
    except ValueError:
        print("Invalid Input.")
        print("Please bet with whole dollars, we do not accept change!\n")
        red_black(cash)          
    
# Function that deals with deciding whether a number is high or low in roulette.       
def high_low(cash):
    low = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    high = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    number = random.randint(1,36)
    try:
        bet = int(input("How much would you like to bet?  $"))
        if bet > cash:
            print("You do not have enough money in the bank!")
            high_low(cash)
        if bet <= cash:
            pick = input("Choose: (H)igh or (L)ow.  ").lower()
            if pick == 'l':
                if number in low:
                    print("The winning number:", number,"\n Congratulations, you win!\n")
                    cash = cash + bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
                if number in high:
                    print("The winning number:", number,"\n Sorry, you lose.\n")
                    cash = cash - bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
            if pick == 'h':
                if number in high:
                    print("The winning number:", number,"\n Congratulations, you win!\n")
                    cash = cash + bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
                if number in low:
                    print("The winning number:", number,"\n Sorry, you lose.\n")
                    cash = cash - bet
                    print("Your new total is :  $", cash)
                    play_again(cash)
            else:
                print("Invalid Input. Try again!")
                high_low(cash)
    except ValueError:
        print("Invalid Input.")
        print("Please bet with whole dollars, we do not accept change!\n")
        high_low(cash)       

# My roulette function which aks the player what they want to bet on and then sends them to the
# right function above.
def roulette(cash):
    if cash <=0:
        print("You need to add funds to play!")
        banker(cash)
    if cash > 0:
        print("\n")
        bettype = input("Choose a type of bet: (C)ategory or (N)umbers:  ").lower() 
        if bettype == 'c':    
            category = input("What would you like to bet on? \n Valid choices: (1)even/odd, (2)red/black, (3)high/low.  ")
            if category == "1":
                even_odd(cash)
            if category == "2":
                red_black(cash)
            if category == "3":
                high_low(cash)
            else:
                print("Invalid Input. Try again!")
                roulette(cash)
        if bettype == 'n':
            number_pick(cash)
        else:
            print("Invalid Input. Try again!")
            roulette(cash)
        
ITEMS = ["\u001b[31mAPPLE\u001b[0m", "\033[0;34mBERRY\u001b[0m", "\033[1;33mLEMON\u001b[0m", "\033[0;32mMELON\u001b[0m", "\033[0;35mGRAPE\u001b[0m", "\033[0;33mMEGA\u001b[0m"]

# My slot machine function which initializes the 3 wheels and then sends them to the spinner
# function and then sends the results of the 'spin' to the results function which evaluates them.
def slot(cash):  
    wheel1 = None
    wheel2 = None
    wheel3 = None
    print("\nWinning combinations:\n MEGA\tMEGA\tMEGA\t\tpays\t$250\n APPLE\tAPPLE\tAPPLE/MEGA\tpays\t$20\n GRAPE\tGRAPE\tGRAPE/MEGA\tpays\t$15\n ORANGE\tORANGE\tORANGE/MEGA\tpays\t$10\n APPLE\tAPPLE\tAPPLE\t\tpays\t$7\n APPLE\tAPPLE\t  -\t\tpays\t$5\n APPLE\t  -\t  -\t\tpays\t$2")   
    if cash <=0:
        print("You need to add funds to play!")
        banker(cash)
    if cash > 0:
        spin = input("\n Press S to spin the wheel!!!  ").lower()
        if spin == 's':
            wheel1 = spinner()
            wheel2 = spinner()
            wheel3 = spinner()
            results(wheel1, wheel2,wheel3, cash)
        else:
            print("Invalid Input. Try again!")
            slot(cash)

# My spinner function which randomizes the 3 wheels.
def spinner():
    itemnumber = random.randint(0, 5)
    return ITEMS[itemnumber]

# My function which evalutes the newly spun wheels looking for winning combinations.
def results(wheel1, wheel2, wheel3, cash):
    if((wheel1 == "BERRY") and (wheel2 != "BERRY")):
        cash = cash +1
        print("\n",wheel1, '\t',wheel2, '\t',wheel3,"\n")
        print("You win $2!")
        print("Your new total is :  $", cash)
        play_again(cash) 
    elif((wheel1 == "BERRY") and (wheel2 == "BERRY") and (wheel3 != "BERRY")):
        cash = cash +1
        print("\n",wheel1, '\t',wheel2, '\t',wheel2,"\n")
        print("You win $5!")
        print("Your new total is :  $", cash)
        play_again(cash) 
    elif((wheel1 == "BERRY") and (wheel2 == "BERRY") and (wheel3 == "BERRY")):
        cash = cash +1
        print("\n",wheel1, '\t',wheel2, '\t',wheel3,"\n")        
        print("You win $7!")
        print("Your new total is :  $", cash)
        play_again(cash) 
    elif((wheel1 == "MELON") and (wheel2 == "MELON") and ((wheel3 == "MELON") or (wheel3 == "MEGA"))):
        cash = cash +1
        print("\n",wheel1, '\t',wheel2, '\t',wheel3,"\n")
        print("You win $10!")
        print("Your new total is :  $", cash)
        play_again(cash) 
    elif((wheel1 == "GRAPE") and (wheel2 == "GRAPE") and ((wheel3 == "GRAPE") or (wheel3 == "MEGA"))):
        cash = cash +1
        print("\n",wheel3, '\t',wheel2, '\t',wheel3,"\n")
        print("You win $15!")
        print("Your new total is :  $", cash)
        play_again(cash) 
    elif((wheel1 == "APPLE") and (wheel2 == "APPLE") and ((wheel3 == "APPLE") or (wheel3 == "MEGA"))):
        cash = cash +1
        print("\n",wheel1, '\t',wheel2, '\t',wheel3,"\n")
        print("You win $20!")
        print("Your new total is :  $", cash)
        play_again(cash) 
    elif((wheel1 == "MEGA") and (wheel2 == "MEGA") and (wheel3 == "MEGA")):
        cash = cash + 250
        print("\n",wheel1, '\t',wheel2, '\t',wheel3,"\n")        
        print("You win $250!")
        print("Your new total is :  $", cash)
        play_again(cash) 
    else:
        cash = cash -1
        print("\n",wheel1, '\t',wheel2, '\t',wheel3,"\n")        
        print("Sorry, you lose.")
        print("Your new total is :  $", cash)
        play_again(cash) 


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*8

# My function that gives the facecards their values.
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 1:
            card = "A"
        hand.append(card)
    return hand

# My main bank function which collects the money you input and then sends you tp the game you want to play
def banker(cash):
    response = True
    while response == True:
        print("\nYour current balance is $",cash)
        choice = input("Would you like to add funds? [Y]es or [N]o?  "  ).lower()
        if choice == 'y':
            try:
                add = int(input("How much money would you like to add?  $"))
                cash = cash + add
                print("Okay, your new total is:  $",cash)
                games = input("\nWhat game would you like to play: (R)oulette, (B)lackjack, or (S)lots?  ").lower()
                if games =='b':
                    BJ(cash)
                if games =='r':
                    roulette(cash)
                if games == 's':
                    slot(cash)
                else:
                    print("Invalid Input. Try again!")
                    continue
            except ValueError:
                print("Invalid Input.")
                print("We only accept whole dollars, no change!\n")
                banker(cash)
        if choice=='n':
            print("Okay, your balance is:  $",cash)
            games = input("\nWhat game would you like to play: (R)oulette, (B)lackjack, or (S)lots?  ").lower()
            if games =='b':
                BJ(cash)
            if games =='r':
                roulette(cash)
            if games == 's':
                slot(cash)
            else:
                print("Invalid Input. Try again!")
                continue
        else:
            print("Invalid Input. Try again!")
            continue

# My function which every game sends you to after completion. It then asks you if you want to play again and 
# what game you want to play.
def play_again(cash):
    again = input("\nDo you want to play again? (Y)es or (N)o :  ").lower()
    if again == 'y':
        gametype = input("What game would you like to play: (R)oulette, (B)lackjack, or (S)lots?  ").lower()
        if gametype == 'b':
            dealer_hand = []
            player_hand = []
            deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*8
            BJ(cash)
        if gametype == 'r':
            roulette(cash)
        if gametype == 's':
            slot(cash)
        else:
            print("Invalid Input. Try again!")
            play_again(cash)
    if again == 'n':
        print("\nYour ending balance is:  $",cash,"\nBring your ticket to the cashier's desk to cash out. Have a great day!\n")
        exit()
    else:
        print("Invalid Input. Try again!")
        play_agin(cash)

# Function that calculates the toal value of an inputted hand.
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: 
                total+= 1
            else: 
                total+= 11
        else: 
            total += card
    return total

# Function that deals with hitting a hand when the player asks for a hit.
def hit(hand):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 1:
        card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

# Function that formats the way the hands are outputted.
def print_hands(dealer_hand, player_hand):
    print ("\nThe dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

# Function to check for blackjack upon initial dealing of the hands.
def blackjack(dealer_hand, player_hand, cash, bet):
    if total(player_hand) == 21:
        print_hands(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        cash = cash + bet
        print("Your new total is :  $", cash)
        play_again(cash)
    elif total(dealer_hand) == 21:
        print_hands(dealer_hand, player_hand)     
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        cash = cash - bet
        print("Your new total is :  $", cash)
        play_again(cash)

# Function which deals with determing the outcome of the game based on the players and the dealers hands.
def score(dealer_hand, player_hand, cash, bet):
    if total(player_hand) == 21:
        print_hands(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        cash = cash + bet
        print("Your new total is :  $",cash)
    elif total(dealer_hand) == 21:
        print_hands(dealer_hand, player_hand)     
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        cash = cash - bet
        print("Your new total is :  $",cash)
    elif total(player_hand) > 21:
        print_hands(dealer_hand, player_hand)
        print ("Sorry. You busted. You lose.\n")
        cash = cash - bet
        print("Your new total is :  $",cash)
    elif total(dealer_hand) > 21:
        print_hands(dealer_hand, player_hand)            
        print ("Dealer busts. You win!\n")
        cash = cash + bet
        print("Your new total is :  $",cash)
    elif total(player_hand) < total(dealer_hand):
        print_hands(dealer_hand, player_hand)
        print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
        cash = cash - bet
        print("Your new total is :  $",cash)
    elif total(player_hand) > total(dealer_hand):
        print_hands(dealer_hand, player_hand)            
        print ("Congratulations. Your score is higher than the dealers. You win!\n") 
        cash = cash + bet
        print("Your new total is :  $", cash)
    play_again(cash)     

#Main blackjack functionthat uses all of the above functions.   
def BJ(cash):
    if cash <=0:
        print("You need to add funds to play!")
        banker(cash)
    if cash > 0:
        try:
            bet = int(input("How much would you like to bet on this game?  $"))
            print("\n")
            if bet > cash:
                print("You do not have enough money in the bank!")
                BJ(cash)
            if bet <= cash:   
                dealer_hand = deal(deck)
                player_hand = deal(deck)
                print ("The dealer is showing a " + str(dealer_hand[0]))
                print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
                blackjack(dealer_hand, player_hand, cash, bet)
                while True:
                    choice = input("Do you want to [H]it or [S]tand?  ").lower()
                    if choice == 'h':
                        hit(player_hand)
                        print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
                        if total(player_hand)>21:
                            print_hands(dealer_hand, player_hand)
                            print('You busted!')
                            cash = cash - bet
                            print("Your new total is :  $", cash)
                            play_again(cash)
                    elif choice == 's':
                        print("\n")
                        while total(dealer_hand) < 17:
                            hit(dealer_hand)
                            if total(dealer_hand) > 21:
                                print_hands(dealer_hand, player_hand)
                                print('Dealer busts, you win!')
                                cash = cash + bet
                                print("Your new total is :  $", cash)
                                play_again(cash)
                            else:
                                continue
                        score(dealer_hand,player_hand,cash,bet)
                    else:
                        print("Invalid Input. Try again!")
                        continue
        except ValueError:
            print("Invalid Input.")
            print("Please bet with whole dollars, we do not accept change!\n")
            BJ(cash)

# My main function which deals with formatting the welcme screen.
if __name__ == "__main__":
    clear()
    print('\033[31mWELCOME TO THE PYTHON CASINO!!!\n\033[0m')
    print("Note:We only accept whole dollars. No change please!\n")
    print("\033[4mWinnings:\033[0m\n\033[1mROULETTE:\033[0m \n -For a category(ex:even/odd):Double your wager! \n -For a number: 36 times your wager!\n\033[1mBLACKJACK:\033[0m\n -Double your wager!\n\033[1mSLOTS:\033[0m\n -Win between $2 and $250!")
    cash = 0
    banker(cash)
