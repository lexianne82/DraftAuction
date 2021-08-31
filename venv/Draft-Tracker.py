import Include.Reference as Values

current_team = 0
current_money = Values.TOTAL_MONEY
print("Do you have an keepers?")
answer = input("Y or N?")
answer = answer.capitalize()
if answer == "Y":
    print("How many?")
    keepers = input("Number of keepers: ")
else:
    keepers = 0

entered = 0
while entered < keepers:
    current_team = current_team + 1
    entered = entered + 1

Values.SPEND = input("How much money would you like availabe each round? ")
while current_team < Values.TOTAL_PLAYERS:
    print("You still need the following players: ")
    print(f'{current_positions[Values.POSITION["QB"]]} Quarterbacks')
    print(f'{current_positions[Values.POSITION["WR"]]} Wide Recievers')
    print(f'{current_positions[Values.POSITION["RB"]]} Running Backs')
    print(f'{current_positions[Values.POSITION["TE"]]} Tight Ends')
    print(f'{current_positions[Values.POSITION["K"]]} Kickers')
    print(f'{current_positions[Values.POSITION["DEF"]]} Defense')
    print()

    rounds_left = Values.TOTAL_PLAYERS - current_team

    Values.isFeezable(current_money, rounds_left)

    max_spend = current_money - (rounds_left * int(Values.SPEND))

    print(f'In order to have ${money} remaining for each round you should not spend more than ${max_spend} this round')
    spent = input("How much did you spend on this player? ")

print("Thank you for drafting. Please choose an option from the list below: ")
print("1. Show Team")
print("2. Start Over")
print("3. Exit")
input("Selcection: ")