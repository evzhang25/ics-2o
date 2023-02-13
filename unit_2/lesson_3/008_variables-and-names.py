team = "Toronto Blue Jays"                  # team is assigned "Toronto Blue Jays"
current_date = "July 18, 2021"              # current_date is assigned "July 18, 2021"
player = "Vladimir Guerrero Jr."            # player is assigned "Vladimir Guerrero Jr."
home_runs_to_date = 31                      # home_runs_to_date is assigned 31
games_played = 88                           # games_played is assigned 88
total_season_games = 162                    # total_season_games is assigned 162
home_run_record = 73                        # home_run_record is assigned 73

# games_remaining is assigned total_season_games - games_played = 162 - 88 = 74
games_remaining = total_season_games - games_played
# home_runs_per_game is assigned home_runs_to_date / games_played = 31 / 88 = 0.3522727272727273
home_runs_per_game = home_runs_to_date / games_played
# projected_home_runs is assigned home_runs_per_game * total_season_games = 57.06818181818182
projected_home_runs = home_runs_per_game * total_season_games
# can_break_record is assigned if projected_home_runs > home_run_record = False
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game, 2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs, 2)} home runs this season.")

# 2.    The reason why the programmer left two empty lines was to separate the code to make it easier to read.
# 4.    The variable names are clear --> The reader/programmer can easily understand the purpose of the variable
#       and can confirm if the value is correct