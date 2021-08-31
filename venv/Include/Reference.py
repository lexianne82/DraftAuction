TOTAL_MONEY   = 150
SPEND         = 0
QB_TOTAL      = 2
WR_TOTAL      = 5
RB_TOTAL      = 4
TE_TOTAL      = 2
K_TOTAL       = 2
DEF_TOTAL     = 2
TOTAL_PLAYERS = 17
REQ_QB        = 1
REQ_WR        = 3
REQ_RB        = 2
REQ_TE        = 1
REQ_K         = 1
REQ_DEF       = 1
Team = []
Positions_left = [QB_TOTAL, WR_TOTAL, RB_TOTAL, TE_TOTAL, K_TOTAL, DEF_TOTAL]
POSITION = { "QB" : 0,
             "WR" : 1,
             "RB" : 2,
             "TE" : 3,
             "K"  : 4,
             "DEF": 5}

def isFeezable(current_money, rounds_left):
    feezable = False
    while not feezable:
        divisable = int(current_money/rounds_left)
        if divisable >= int(SPEND):
            feezable = True
        else:
            print("You don't have enough money left!")
            SPEND = input("How much do you now want to spend on each round? ")

def addPlayer(current_team):
    name = input("Enter name of player: ")
    positon = input("Enter player positon: ")
    Team[current_team] = (name, positon)