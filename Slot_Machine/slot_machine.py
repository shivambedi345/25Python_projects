# python slot machine
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🥂', '🍽️']
    
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
    
def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] =='🍒':
            return bet * 4
        elif row[0] == '🍉':
            return bet * 6
        elif row[0] == '🍋':
            return bet * 7
        elif row[0] == '🥂':
            return bet * 3
        elif row[0] == '🍽️':
            return bet * 25
    return 0
    

def main():
    balance = 100
    
    print("***********************")
    print("Welcome to python slot")
    print("Symbols: 🍒 🍉 🍋 🥂 🍽️ ")
    print("***********************")
    
    while balance > 0:
        print(f"Current balance : ${balance}")
        
        bet = input("Place your bet amount : ")
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("insufficient fund:")
            continue
        
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")
        
        balance += payout
        
        play_again = input("Do you want to ply again (Yes/No):").upper()
        if play_again != 'Y':
            break
    print("***********************************************")    
    print(f"Game Over ! Your final balance is : ${balance}")
    print("***********************************************")       
    
if __name__ == '__main__':
    main()
