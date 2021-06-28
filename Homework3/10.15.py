# Mauricio Corado 1254732

class Team:                     # creates a class and initializes
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):       # method calculates win percentage
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent

if __name__ == '__main__':
    team = Team()
    teamname = input()            # receives input
    teamwins = int(input())
    team_losses = int(input())

    team.team_name = teamname
    team.team_wins = teamwins
    team.team_losses = team_losses
# if statement to determine if team is above 500

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team {} has a winning average!'.format(teamname))
    else:
        print('Team {} has a losing average.'.format(teamname))