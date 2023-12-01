import json
from Player import Player

class ScoreManager:
    
    def __init__(self, filename):
        self.filename = filename
        self.user_scores = self.load_scores()

    def load_scores(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_scores(self):
        with open(self.filename, 'w') as file:
            json.dump(self.user_scores, file)
        
    def add_user(self, username):
        # Check if the username already exists in the hashmap
        if username not in self.user_scores:
            # If not, add the username with a default score of 0
            self.user_scores[username] = 0
            print(f"User {username} added with a default score of 0.")
        else:
            print(f"User {username} already exists.")
        
    # Function to update scores
    def update_scores(self, player):
        if player.username in self.user_scores:
            if player.win == 1:
                self.user_scores[player.username] += 50
            elif player.win == 0 and player.score <= 0:
                self.user_scores[player.username] = 0
            elif player.win == 0:
                self.user_scores[player.username] -= 50
            
            player.score = self.user_scores[player.username]
            self.save_scores()
    
    

