import json
import time 
import csv
import requests

#get form, current price, selected%, lastGW points, totalPoints, ICT, influence, create, threat, GW in, GW out, bonus points
def create_table_all_player_all_stats():
    """ Retrieve complete player data
    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = ''
    while response == '':
        try:
            response = requests.get(url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    
    all_data = json.loads(response.text) ### this is a list
    player_data = sorted(all_data["elements"], key=lambda x: x["id"])
    team_data=all_data["teams"]
    position_map={1:"GK",2:"DEF",3:"MID",4:"FWD"}

    columns=["web_name", "team", "element_type", "form", "now_cost", "selected_by_percent", "event_points", "total_points", "ict_index", "influence", "creativity", "threat", "transfers_in", "transfers_out", "bonus"]
    csvPath="C:/Users/dhruv/OneDrive/Desktop/Projects/fantasy-team/data/23-24/players_stats.csv"
    with open(csvPath, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns)

        
    with open(csvPath, "a", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        for json_data in player_data:
            values = [json_data.get(c, '') for c in columns]
            values[1]=[team["name"] for team in team_data if team.get("id") == values[1]][0]
            values[2]=position_map[values[2]]
            csv_writer.writerow(values)


    all_data = json.loads(response.text)

    all_json_objects=json.dumps(all_data, indent=4)


create_table_all_player_all_stats()
