"""
File:           scoring.py
Author:         Matt Barton V244576
Description:
handles scores by reading in a json file if it exists and then returning the highest score
saves new high scores.
"""
import os
import json
from player import Player, from_dict


def get_high_score():
    """
    Reads in saved player data and returns the highest scoring player

    """
    highest_player = Player
    highest_player.score = 6
    highest_player.name = 'nobody special'
    players = []

    # check if the file exists
    if check_json_file('scores.json'):
        with open('scores.json') as json_file:
            # read in from file
            data = json_file.read()
            # load to json string
            json_data = json.loads(data)
            # loads to a dictionary
            players_dict = json_data['players']
            # for each player in dictionary
            for player_dict in players_dict:
                # convert to player object
                player = from_dict(player_dict)
                # add to player object list
                players.append(player)
                # for each player in object list
            for a_player in players:
                # check score against current highest score
                if int(highest_player.score) > a_player.score:
                    # if the current players score is lower (least guesses)
                    # this is the best score (called highest)
                    highest_player = a_player
    # return the player object with the highest (least counts) score
    return highest_player


def save_high_score(_name, _score, att_message, att_button, att_name):
    """
    Saves the score and player name
    Checks against current saved scores and tells the player if theirs is the highest
    """
    # initialise a default player with a score above the possible score
    highest_player = Player
    highest_player.score = 6
    highest_player.name = 'nobody special'
    # new player with the interface details
    new_player = Player(_name, _score)
    # new player list
    players = []
    # blank message string
    message = ""

    # check if the file exists
    if check_json_file('scores.json'):
        with open('scores.json') as json_file:
            # read in from file
            data = json_file.read()
            # load to json string
            json_data = json.loads(data)
            # load to dictionary
            players_dict = json_data['players']
            # for each player in dictionary
            for player_dict in players_dict:
                # convert to player object
                player = from_dict(player_dict)
                # add to player object list
                players.append(player)
            # go through each and find the player with the least guesses to win
            for a_player in players:
                if int(highest_player.score) > a_player.score:
                    highest_player = a_player
            # if new player has highest score save and tell them
            if highest_player.score > new_player.score:
                players.append(new_player)
                message = "New High "
    # if no file then create new one
    else:
        players = [new_player]
        message = "First High "
    # check that name is not the default
    if _name != 'nobody special':
        with open('scores.json', 'w') as output:
            # add players to a dictionary
            data = [Player.to_dict() for Player in players]
            # convert dictionary to json string
            json_data = json.dumps({"players": data})
            # write to file
            output.write(json_data)
            # finish message
            message += "Score - Saved!"
            # disable the button and the name entry
            att_button["state"] = "disabled"
            att_name["state"] = "disabled"
    # if the name is blank ask for name
    elif _name == "":
        message = "No Name entered - Enter a Name to Save!"
    # if default name ask for another
    else:
        message = "Default Name - Choose a Different Name!"
    # set message to label text
    att_message['text'] = message


def check_json_file(file_name):
    """
    Checks if json file exists using os path exists method
    """
    return os.path.exists(file_name)



