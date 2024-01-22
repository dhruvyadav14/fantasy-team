###read in the csv file to get all players###
from cmath import inf
import csv
from pulp import LpProblem, LpVariable, LpInteger, LpStatus, lpSum, LpMaximize

"""
how do we calculate the best possible team? a team has 2 GKs, 5 DEFs, 5 MIDs, 3 FWDs
we will make a decision that we dont care about bench players
we will also make a decision to play a 3-5-2. midfielders get the most points. 
now, lets solve the knapsack problem. lets maximize number of points while taking into account the total budget

calculate the cheapest GK, the 2 cheapest defenders, and the cheapest FWD. sum all that up and subtract it from 100
this is our new budget
"""

def best_team():
    csvFilePath="C:/Users/dhruv/OneDrive/Desktop/Projects/fantasy-team/epl/data/23-24/players_stats.csv"
    playerDict = {}
    with open(csvFilePath, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        minGK=("",inf) #get the cheapest GK
        minFWD=("",inf) #get the cheapest FWD
        minDEF1=("",inf)
        minDEF2=("",inf) #get the 2 cheapest DEFs
        budget=100

        for row in csv_reader:
            name = row["web_name"]
            points = int(row["total_points"])
            cost = float(row["now_cost"])/10
            position = row["element_type"]
            if position == "GK" and cost < minGK[1]:
                minGK = (name,cost)
            elif position == "FWD" and cost < minFWD[1]:
                minFWD = (name,cost)
            if position == "DEF" and cost < minDEF1[1]:
                minDEF2 = minDEF1
                minDEF1 = (name,cost)
            elif position == "DEF" and cost < minDEF2[1]:
                minDEF2 = (name,cost)
            # this is pretty janky. look up how to use heapq to get the two smallest values
            playerDict[name] = [position, points, cost]
        playerDict.pop(minGK[0])
        playerDict.pop(minFWD[0])
        playerDict.pop(minDEF1[0])
        playerDict.pop(minDEF2[0])
        # get rid of all the min guys
        budget=budget - minGK[1]-minFWD[1]-minDEF1[1]-minDEF2[1]
    print(playerDict)
    result = maximize_points(playerDict, budget)
    # Print the selected players
    for player in result:
        print(f"Selected {player}: Position = {playerDict[player][0]}, Cost = {playerDict[player][2]}, Points = {playerDict[player][1]}")

def maximize_points(players, budget_limit):
    positions = ["GK", "DEF", "MID", "FWD"]
    num_required = {"GK": 1, "DEF": 3, "MID": 5, "FWD": 2}

    # Create a linear programming problem
    prob = LpProblem("MaximizePoints", LpMaximize)

    # Create binary decision variables for each player
    player_vars = LpVariable.dicts("Player", players.keys(), 0, 1, cat=LpInteger)

    # Objective function: maximize total points
    prob += lpSum(player_vars[player] * players[player][1] for player in players), "TotalPoints"

    # Budget constraint
    prob += lpSum(player_vars[player] * players[player][2] for player in players) <= budget_limit, "BudgetLimit"

    # Position constraints
    for position in positions:
        prob += lpSum(player_vars[player] for player in players if players[player][0] == position) == num_required[position], f"{position}Requirement"

    # Solve the linear programming problem
    prob.solve()

    # Retrieve the selected players
    selected_players = [player for player in players if player_vars[player].value() == 1]

    return selected_players

best_team()