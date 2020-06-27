import sys

class Team():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.goals_scored = 0
        self.goals_against = 0
        self.games_played = 0

    def __str__(self):
        return f'{self.name} {self.points}p, {self.games_played}g ({self.wins}-{self.ties}-{self.losses}), {self.goal_difference()}gd ({self.goals_scored}-{self.goals_against})'

    def __lt__(self, other):
        if self.points < other.points:
            return False
        if self.points > other.points:
            return True
        if self.wins < other.wins:
            return False
        if self.wins > other.wins:
            return True
        if self.goal_difference() < other.goal_difference():
            return False
        if self.goal_difference() > other.goal_difference():
            return True
        if self.goals_scored < other.goals_scored:
            return False
        if self.goals_scored > other.goals_scored:
            return True
        if self.games_played < other.games_played:
            return True
        if self.games_played > other.games_played:
            return False
        return self.name.lower() < other.name.lower()

    def add_game(self, goals_scored, goals_against, result):
        self.games_played += 1
        self.goals_scored += goals_scored
        self.goals_against += goals_against
        if result == 'W':
            self.wins += 1
            self.points += 3
        elif result == 'T':
            self.points += 1
            self.ties += 1
        elif result == 'L':
            self.losses += 1

    def goal_difference(self):
        return self.goals_scored - self.goals_against


for tournament in range(int(sys.stdin.readline())):
    tournament_name = sys.stdin.readline()[:-1]
    stats = {}
    for i in range(int(sys.stdin.readline())):
        name = sys.stdin.readline()[:-1]
        stats[name] = Team(name)
    for i in range(int(sys.stdin.readline())):
        game = sys.stdin.readline()[:-1]
        left, right = game.split('@')
        left_team, left_score  = left.split('#')
        right_score, right_team = right.split('#')
        left_score = int(left_score)
        right_score = int(right_score)

        if left_score > right_score:
            stats[left_team].add_game(left_score, right_score, 'W')
            stats[right_team].add_game(right_score, left_score, 'L')
        elif right_score > left_score:
            stats[left_team].add_game(left_score, right_score, 'L')
            stats[right_team].add_game(right_score, left_score, 'W')
        else:
            stats[left_team].add_game(left_score, right_score, 'T')
            stats[right_team].add_game(right_score, left_score, 'T')
    ordered = sorted(stats.values())
    if tournament > 0:
        print()
    print(tournament_name)
    for i in range(len(ordered)):
        print(f'{i+1}) {ordered[i]}')
