import json
from flask import Flask,render_template,request,redirect,flash,url_for
<<<<<<< HEAD
from datetime import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions
=======
from utils import loadClubs, loadCompetitions, booked_places
>>>>>>> master


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
places_booked = booked_places(competitions, clubs)

def sort_competitions_date(comps):
    past = []
    present = []
    for comp in comps:
        if datetime.strptime(comp['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            past.append(comp)
        elif datetime.strptime(comp['date'], '%Y-%m-%d %H:%M:%S') >= datetime.now():
            present.append(comp)
    return past, present

past_competitions, present_competitions = sort_competitions_date(competitions)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, past_competitions=past_competitions, present_competitions=present_competitions)
    except IndexError:
        if request.form['email'] == '':
            flash("Please enter your email.", 'error')
        else:
            flash("No account related to this email.", 'error')
    
    list_club = []
    for c in clubs:
        list_club.append(c["email"])
        
    if request.form['email'] == '':
        flash("Please enter your email.")
        return render_template('index.html'), 403
    elif request.form['email'] not in list_club:
        flash("No account related to this email.")
        return render_template('index.html'), 403
    else:
        club_list = []
        for i in clubs:
            if i['email'] == request.form['email']:
                club_list.append(i)
        email_club = club_list[0]
        return render_template('welcome.html', club=email_club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):

    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        if datetime.strptime(found_competition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            flash("This competition is over.", 'error')
            return render_template(
                'welcome.html',
                club=club,
                past_competitions=past_competitions,
                present_competitions=present_competitions
            ), 403
        return render_template('booking.html', club=found_club, competition=found_competition)
    print("toto")
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again", 'error')
        return render_template(
            'welcome.html',
            club=club,
            past_competitions=past_competitions,
            present_competitions=present_competitions
        ), 403



@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    
    """purchase of competition places by a club.
    Retrieves the selected competition and club,
    from the `competitions` and `clubs` lists based on the form data submitted by the user.
    If the number of places required exceeds the number of points the club has,
    a message is added to the user session and the home page is displayed.
    Otherwise, the number of remaining places for the competition is updated,
    and the number of points remaining for the club is reduced.
    A message is added to the user session and the home page is displayed."""
    
    # Recovery of the chosen competition
    competition_name = request.form['competition']
    for competition in competitions:
        if competition['name'] == competition_name:
            selected_competition = competition
            break
    
    # Club recovery
    club_name = request.form['club']
    for club in clubs:
        if club['name'] == club_name:
            selected_club = club
            break

    places_required = int(request.form['places'])

    if places_required > int(club['points']):

            # Adding a notification message to the user session
            flash('You don\'t have enough points.')
            flash(f"You have that : {club['points']} Points available")
            
            # Home page display
            return render_template('booking.html', club=club, competition=competition)
    elif places_required > 12:
        
        # Adding a notification message to the user session
        flash('You can\'t book more than 12 places in a competition.')
        
        # Home page display
        return render_template('booking.html', club=club, competition=competition)
        return render_template('booking.html', club=club, competition=competition), 400
    else:
        
        update_booked_places(selected_competition, selected_club, places_required)
        
        # Update of the number of remaining places for the competition
        selected_competition['numberOfPlaces'] = int(selected_competition['numberOfPlaces']) - places_required 
        
        # Updating the number of points remaining for a club
        club['points'] = int(club['points']) - places_required
        
        # Adding a notification message to the user session
        flash('booking complete')
        
        # Home page display
        return render_template('welcome.html', club=club, competitions=competitions)



def update_booked_places(competition, club, places_required):
    for item in places_booked:
        
        #checks if the name of the competition of the item element is the same as that of the competition passed in competition parameter
        if item['competition'] == competition['name']:
            
            #the item element is the same as the name of the club passed as the club parameter
            if item['booked'][1] == club:
                
                # checks if the number of places reserved plus the number of places requested is <= 12
                if item['booked'][0] + places_required <= 12:
                    
                    #updates the number of places reserved by adding the number of places requested
                    item['booked'][0] += places_required
                    break
                else:
                    raise ValueError("You can't book more than 12 places in a competition.")


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))