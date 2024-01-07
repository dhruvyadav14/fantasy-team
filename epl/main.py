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
    
    data = sorted(json.loads(response.text)["elements"], key=lambda x: x["id"]) ### this is a list
    json_object = json.dumps(data, indent=4) ### this is a string
    print(data[354])
    columns=["web_name", "form", "now_cost", "selected_by_percent", "event_points", "total_points", "ict_index", "influence", "creativity", "threat", "transfers_in", "transfers_out", "bonus"]
    
    with open("players_stats.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(columns)

        
    with open("players_stats.csv", "a", newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        for json_data in data:
            values = [json_data.get(c, '') for c in columns]
            csv_writer.writerow(values)

