from View.UI import UI


class Main():

    UI().run()
#    nbaStat = NbaStatAnalyser(season_id='2021-22', per_mode='per', lastNGames='10')
#    point_score_relevant_data = nbaStat.pullData(point_score_relevant_variables)
#    point_score_relevant_data_list = nbaStat.filterDataToList(point_score_relevant_data)
#    clusterAnalyser = ClusterAnalyser(nbaStat)
#    data = clusterAnalyser.averageAwayFromMean(point_score_relevant_data_list)
#    print(data)

if __name__ == '__main__':
    Main()