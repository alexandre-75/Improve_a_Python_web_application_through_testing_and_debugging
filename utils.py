import json
from datetime import datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions
    
def booked_places(args_competitions, args_clubs):
    """
     Creates a list of initial seat reservations for each combination of competitions and clubs.
     args:
         args_competitions(list): A list of dictionaries representing competitions

     Returns:
         list: A list of dictionaries
     """
    places = []
    for comp in args_competitions:
        for club in args_clubs:
            places.append({'competition': comp['name'], 'booked': [0, club['name']]})
    return places

def sort_competitions(args_competitions):
    
    """
     Sort past and future competitions by date.

     args:
     - args_competitions: a list of dictionaries containing the details of each competition.

     Returns:
     - past_competitions: a list containing dictionaries of competitions that took place before the current date and time.
     - future_competitions: a list containing the dictionaries of the competitions that will take place from the current date and time.
     """
    
    past_competitions = []
    future_competitions = []
    
    for i in args_competitions:
        if datetime.strptime(i['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            past_competitions.append(i)
        elif datetime.strptime(i['date'], '%Y-%m-%d %H:%M:%S') >= datetime.now():
            future_competitions.append(i)
            
    return past_competitions, future_competitions