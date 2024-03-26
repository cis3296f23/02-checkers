"""
ScoreManager.py
The ScoreManager File holds the ScoreManager class which is responsible for managing the scores of the players.
"""

import json
from Player import Player

class ScoreManager:
    """
    The ScoreManager class is responsible for managing the scores of the players, and contains functions to add users and update and load scores.
    """
    def __init__(self, filename):
        """
        The init function initializes the ScoreManager class with a filename and loads the scores from the json file.
        """
        self.filename = filename
        self.user_scores = self.load_scores()

    def load_scores(self):
        """
        The load_scores function loads the scores from the json file and returns the scores.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_scores(self):
        """
        The save_scores function saves the scores to the json file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.user_scores, file)
        
    def add_user(self, username):
        """
        The add user function adds a user to the hashmap with a default score of zero if the user does not already exist.
        """
        # Check if the username already exists in the hashmap
        if username not in self.user_scores:
            # If not, add the username with a default score of 0
            self.user_scores[username] = 0
            print(f"User {username} added with a default score of 0.")
        else:
            print(f"User {username} already exists.")
        
    def update_scores(self, player):
        """
        The update scores function updates the scores of the players based on the outcome of the game. Calls the save scores function to save the scores to the json file.
        """
        if player.username in self.user_scores:
            if player.win == 1:
                self.user_scores[player.username] += 50
            else:
                if player.score == 0:
                    pass
                else:                    
                    self.user_scores[player.username] -= 50
            
            player.score = self.user_scores[player.username]

            self.save_scores()


