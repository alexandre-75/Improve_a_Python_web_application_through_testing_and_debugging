import json

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
