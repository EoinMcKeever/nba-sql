import pandas as pd

years = range(2022,2024)


#when searching for a player input their first and last name only.
player_name = 'Jayson tatum'
players_name_extension = 'Jayson tatum'.lower().split(" ")

extension = players_name_extension[1][0] + "/" + players_name_extension[1][0:5] + players_name_extension[0][0:2] + "01"
print(extension)

frames = {}
game_by_game_frame = {}
for y in years:        # NBA season to scrape
  year = y
  # URL to scrape, notice f string:
  frames["url" + str(y)] = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"

for y in years:
  year = y
  game_by_game_frame["url" + str(y)] = f"https://www.basketball-reference.com/players/{extension}/gamelog/{year}#all_pgl_basic"

for i in game_by_game_frame:
  x = pd.read_html(game_by_game_frame[i])[7]

  y = x.loc[:,['MP','PTS','AST','TRB','STL','BLK','TOV']]
  relevant_data = y.loc[:,'MP']

  print(relevant_data.array[0])


