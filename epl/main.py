import json
import time 
import requests
import csv

#get form, current price, selected%, lastGW points, totalPoints, ICT, influence, create, threat, GW in, GW out, bonus points
def create_table_all_player_all_stats():
    """ Retrieve the fixtures data for the season
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

    columns=["web_name", "team", "form", "now_cost", "selected_by_percent", "event_points", "total_points", "ict_index", "influence", "creativity", "threat", "transfers_in", "transfers_out", "bonus"]
    
    with open("players_stats.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns)

        
    with open("players_stats.csv", "a", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        for json_data in player_data:
            values = [json_data.get(c, '') for c in columns]
            values[1]=[team["name"] for team in team_data if team.get("id") == values[1]][0]
            csv_writer.writerow(values)


    all_data = json.loads(response.text)

    all_json_objects=json.dumps(all_data, indent=4)

    with open("sample.json", 'w') as json_file:
        json_file.write(all_json_objects)


create_table_all_player_all_stats()
