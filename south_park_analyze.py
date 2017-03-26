import pandas as pd

MAX_SEASON = 18


def read_south_park_data(file_name):
    return pd.read_csv(file_name)


def word_count_by_season_and_episode(df, word, character="", seasons=[], episodes=[]):
    '''
    '''
    count = 0
    character = character.lower()
    word = word.lower()

    for idx, row in df.iterrows():

        # If seasons and episodes are both unspecified,
        # calculate word frequency overall seasons and episodes.
        if seasons == [] and episodes == []:
            if character == "":
                if word in row['Line'].lower():
                    split_line = row['Line'].split()
                    for w in split_line:
                        if word in w.lower():
                            count += 1
            else:
                if word in row['Line'].lower() and character in row['Character'].lower():
                    split_line = row['Line'].split()
                    for w in split_line:
                        if word in w.lower():
                            count += 1

        # If seasons are specified but episodes are not,
        # calculate word frequency by season.
        elif seasons != [] and episodes == []:
            if character == "":
                if any(season == row['Season'] for season in seasons) and word in row['Line'].lower():
                    split_line = row['Line'].split()
                    for w in split_line:
                        if word in w.lower():
                            count += 1
            else:
                if any(season == row['Season'] for season in seasons) and word in row['Line'].lower() and character in row['Character'].lower():
                    split_line = row['Line'].split()
                    for w in split_line:
                        if word in w.lower():
                            count += 1

        # If seasons and episode are specified,
        # calculate word frequency over specific
        # seasons and episodes.
        else:
            if character == "":
                if any(season == row['Season'] for season in seasons) and any(episode == row['Episode'] for episode in episodes) and word in row['Line'].lower():
                    split_line = row['Line'].split()
                    for w in split_line:
                        if word in w.lower():
                            count += 1
            else:
                if any(season == row['Season'] for season in seasons) and any(episode == row['Episode'] for episode in episodes) and word in row['Line'].lower() and character in row['Character'].lower():
                    split_line = row['Line'].split()
                    for w in split_line:
                        if word in w.lower():
                            count += 1
    return count



def character_count_by_season_and_episode(df, character, seasons=[], episodes=[]):
    '''
    '''
    count = 0
    character = character.lower()
    for idx, row in df.iterrows():

        # If seasons and episodes are both unspecified,
        # calculate word frequency overall seasons and episodes.
        if seasons == [] and episodes == []:
            if character in row['Character'].lower():
                count += 1

        # If seasons are specified but episodes are not,
        # calculate word frequency by season.
        elif seasons != [] and episodes == []:
            if any(season == row['Season'] for season in seasons) and character in row['Character'].lower():
                count += 1

        # If seasons and episode are specified,
        # calculate word frequency over specific
        # seasons and episodes.
        else:
            if any(season == row['Season'] for season in seasons) and any(episode == row['Episode'] for episode in episodes) and character in row['Character'].lower():
                count += 1
    return count


def word_count_season_frequency(df, swear_list):
    swear_freq = []
    swear_count = 0
    for sw in swear_list:
        swear_freq.append([])
        for season in range(1, MAX_SEASON + 1):
            output = word_count_by_season_and_episode(df, sw, [str(season)], episodes=[])
            print("SEASON:" + str(season) + " WORD:" + sw + str(output))
            swear_freq[swear_count].append(output)
        swear_count += 1
    return swear_freq


file_name = "sp_season_dialog.csv"
df = read_south_park_data(file_name)

## Example function calls: (uncomment any of the following to run)

# Question: How many times is the word “dude” said in all of the seasons 1 to 18:
#print ( word_count_by_season_and_episode(df, word="dude") )

# Question: How many times is the word “dude” said in all of season 1:
#print( word_count_by_season_and_episode(df, word="dude", seasons=['1']) )

# Question: How many times is the word “dude” said in seasons 1,2,3, and 10:
#print( word_count_by_season_and_episode(df, word="dude", seasons=['1','2','3','10']))

# Question: How many times is the word “dude” said in season 1 and in episodes 1 and 2:
#print( word_count_by_season_and_episode(df, word="dude", seasons=['1'], episodes=['1','2']) )

# Question: How many times is the word “dude” said in all of the seasons 1 to 18 by Cartman:
#print( word_count_by_season_and_episode(df, word="dude", character="Cartman") )

