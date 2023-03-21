import db

def Display_Card(card):
    print(card[0])
    print(card[1])
    print(card[2])

def main():
    print("Blackjack Project")
    money = db.load_money_from_disk();
    print(f"I have {money} dollars")


    card = ["Hearts", "Ace", 11];

    Display_Card(card)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
