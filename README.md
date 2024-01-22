Premier League Fantasy team creator

English Premier League website: https://www.premierleague.com/home

This project aims to solve the [knapsack problem](https://developers.google.com/optimization/pack/knapsack#:~:text=In%20the%20knapsack%20problem%2C%20you,can't%20pack%20them%20all.) using linear programming to create the best team. 
It creates a team with the 3-5-2 formation with bench players completely minimized. 
Data sources from EPL API ("https://fantasy.premierleague.com/api/bootstrap-static/") - the project grabs total points and aims to maximize points while staying in the budget and position constraint.

Next steps:
Take into account form, injury, and fixture rating.

Further steps:
Given a current fantasy team, make recommendations. 
1) Who to captain
2) When to use chips - free hit, triple captain, and bench boost
3) Suggest transfers - if a team has one or two free transfers, should they use it?
