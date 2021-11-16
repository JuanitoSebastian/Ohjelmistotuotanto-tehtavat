class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists

    def assists_and_goals_total(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:25}{self.team:5}{str(self.goals)} + {str(self.assists)} = {str(self.assists_and_goals_total())}"
        #return "%s (%s): %s + %s = %s" % (self.name, self.team, self.goals, self.assists, self.assists_and_goals_total())
