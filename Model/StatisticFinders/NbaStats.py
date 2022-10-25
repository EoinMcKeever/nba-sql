import requests
import pandas as pd
import json
from Utility.StatLabelsVariables import all_player_stat_labels

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

class NbaStatAnalyser():

    def __init__(self, season_id, per_mode,lastNGames):
        self.lastNGames = lastNGames
        self.season_id = season_id
        self.per_mode = per_mode
        self.all_player_stat_labels = all_player_stat_labels
        self.player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames='+lastNGames+'&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+per_mode+'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+season_id+'&SeasonSegment=&SeasonType=Regular Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
        self.current_dataset = self.pullData(all_player_stat_labels)

    def pullData(self, filter_labels):
        response = requests.get(url=self.player_info_url, headers=headers)
        data = json.loads(response.text)
        player_info = data['resultSets'][0]['rowSet']
        df = pd.DataFrame(player_info, columns=self.all_player_stat_labels)
        return df.filter(filter_labels)

    def filterDataToList(self, relevant_data):
        i = 0
        player_data = []
        for name in relevant_data['PLAYER_NAME']:
            player_stats = (relevant_data['PTS'][i])
            player_data.append([name, player_stats])
            i += 1
        return player_data

    def getSeasonId(self):
        return self.season_id

    def setSeasonId(self, season_id):
        self.season_id = season_id

    def getPerMode(self):
        return self.per_mode

    def setPerMode(self, per_mode):
        self.per_mode = per_mode

point_score_relevant_variables = ['PLAYER_NAME', 'TEAM_ID','TEAM_ABBREVIATION','AGE', 'GP', 'W', 'L', 'MIN', 'FGM','FG3M','FG3_PCT', 'FTM','REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA','REB', 'AST', 'TOV', 'STL', 'BLK','PTS']









