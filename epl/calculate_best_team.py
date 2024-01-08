###read in the csv file to get all players###
import csv
from pulp import LpProblem, LpVariable, lpSum, LpMaximize

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
        for row in csv_reader:
            name = row["web_name"]
            points = row["total_points"]
            cost = float(row["now_cost"])/10



# def maximize_points(players, budget_limit):
#     positions = ["GK", "DEF", "MID", "FWD"]
#     num_required = {"GK": 1, "DEF": 3, "MID": 5, "FWD": 2}

#     # Create a linear programming problem
#     prob = LpProblem("MaximizePoints", LpMaximize)

#     # Create binary decision variables for each player
#     player_vars = LpVariable.dicts("Player", players.keys(), 0, 1, LpVariable.integer)

#     # Objective function: maximize total points
#     prob += lpSum(player_vars[player] * players[player][1] for player in players), "TotalPoints"

#     # Budget constraint
#     prob += lpSum(player_vars[player] * players[player][2] for player in players) <= budget_limit, "BudgetLimit"

#     # Position constraints
#     for position in positions:
#         prob += lpSum(player_vars[player] for player in players if players[player][0] == position) == num_required[position], f"{position}Requirement"

#     # Solve the linear programming problem
#     prob.solve()

#     # Retrieve the selected players
#     selected_players = [player for player in players if player_vars[player].value() == 1]

#     return selected_players

# # Example usage:
# players = {
#     "Player1": ["GK", 30.0, 10.0],
#     "Player2": ["GK", 25.0, 8.0],
#     "Player3": ["DEF", 40.0, 15.0],
#     "Player4": ["DEF", 35.0, 12.0],
#     "Player5": ["DEF", 30.0, 10.0],
#     "Player6": ["MID", 50.0, 20.0],
#     "Player7": ["MID", 45.0, 18.0],
#     "Player8": ["MID", 40.0, 15.0],
#     "Player9": ["MID", 35.0, 12.0],
#     "Player10": ["MID", 30.0, 10.0],
#     "Player11": ["FWD", 60.0, 25.0],
#     "Player12": ["FWD", 55.0, 22.0],
# }

# budget_limit = 50.0  # Adjust as needed
# result = maximize_points(players, budget_limit)

# # Print the selected players
# for player in result:
#     print(f"Selected {player}: Position = {players[player][0]}, Cost = {players[player][2]}, Points = {players[player][1]}")


# best_team()