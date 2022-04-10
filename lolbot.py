
from riotwatcher import LolWatcher, ApiError
from champDict import champ_dict

api_key = 'RGAPI-60e0eff4-b205-494c-bd54-f2203ffd1d8d'
watcher = LolWatcher(api_key)
my_region = 'na1'
user_input = ''
mastery_str = ''
count = 0
final_str = ''
champion_mastery = ''
all_champs = ''
max_val = 0
winrate = 0
team_str = ''
indiv_str = ''

me = ''
ranked_stats = ''

def set_me():
    global me
    if user_input != 'None':
        me = watcher.summoner.by_name(my_region, user_input)

def get_ID():
    ID_str = "IDENTIFICATION: \n" + "\n Summoner Name: " + me['name'] + "\n Summoner Level: " + str(me['summonerLevel'])
    return ID_str

def get_stats():
    global ranked_stats
    ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    print(ranked_stats)

def get_solo():
    
    for stats in ranked_stats:
        global winrate
        winrate = stats['wins']/(stats['wins']+stats['losses']) * 100
        # print(i['queueType'])
        if stats['queueType'] == 'RANKED_SOLO_5x5':
            solo_str = "RANKED SOLO: \n" + \
                        "Summoner Name: " + stats['summonerName'] + \
                        "\nRank: " + stats['tier'] + " " + stats['rank'] + \
                        "\nWins - Losses: " + str(stats['wins']) + "-" + str(stats['losses']) + " (" + str(winrate) + "%)"\
                        "\nHot Streak?: " + str(stats['hotStreak'])
            return solo_str 
            break

def get_team():

    global team_str
    team_str = ''
    global indiv_str
    indiv_str = ''

    for stats in ranked_stats:
        global winrate
        winrate = stats['wins']/(stats['wins']+stats['losses']) * 100
        # print(i['queueType'])
        if stats['queueType'] == 'RANKED_SOLO_5x5':
            indiv_str = "RANKED SOLO: \n" + \
                        "Summoner Name: " + stats['summonerName'] + \
                        "\nRank: " + stats['tier'] + " " + stats['rank'] + \
                        "\nWins - Losses: " + str(stats['wins']) + "-" + str(stats['losses']) + " (" + str(winrate) + "%)"\
                        "\nHot Streak?: " + str(stats['hotStreak'])
        
            team_str = team_str + indiv_str            
            return team_str 

def get_flex():
    for stats in ranked_stats:
        # print(i['queueType'])
        if stats['queueType'] == 'RANKED_FLEX_SR':
            flex_str = "RANKED FLEX: \n" + \
                        "Summoner Name: " + stats['summonerName'] + \
                        "\nQueue Type: " + stats['queueType'] + \
                        "\nRank: " + stats['tier'] + " " + stats['rank'] + \
                        "\nWins - Losses: " + str(stats['wins']) + "-" + str(stats['losses']) + \
                        "\nHot Streak?: " + str(stats['hotStreak'])
            return flex_str
                    

def get_mastery():
    global champion_mastery
    champion_mastery = watcher.champion_mastery.by_summoner(my_region, me['id'])

# count = 0
# num = 0
# for champ in champion_mastery:
#     for stat in champion_mastery[count]:
#         print("#", count+1, "Champion Info:", stat, ":", champion_mastery[count][stat])
#     count = count + 1
    global all_champs
    all_champs = champ_dict
# for champID in all_champs:
#     print(champID, all_champs[champID])
    global count
    count = 0

    final_str = ''

    for champ in champion_mastery:

        print(champ)

        # mastery_str = ("\nCHAMPION MASTERY: " + "\n#" + str(count+1) + " Champion Mastery Information:" + \
        #                 "\nChampion ID: " + str(champion_mastery[count]['championId']) + \
        #                 "\nChampion Name: " + all_champs[champion_mastery[count]['championId']] + \
        #                 "\nChampion Points Until Next Level: " + str(champion_mastery[count]['championPointsUntilNextLevel']) + \
        #                 "\nChampion Chest Availability: " + str(champion_mastery[count]['chestGranted']) + \
        #                 "\nChampion Level: " + str(champion_mastery[count]['championLevel']))  

        mastery_str = ("\n#" + str(count+1) + " Champion Mastery Information:" + \
                        "\nChampion ID: " + str(champ['championId']) + \
                        "\nChampion Name: " + all_champs[champ['championId']] + \
                        "\nChampion Points Until Next Level: " + str(champ['championPointsUntilNextLevel']) + \
                        "\nChampion Chest Received?: " + str(champ['chestGranted']) + \
                        "\nChampion Level: " + str(champ['championLevel'])+ "\n")  


        final_str = final_str + mastery_str

        print(final_str)

        count = count + 1
        global max_val
        if count == max_val:
            break

    return final_str 
