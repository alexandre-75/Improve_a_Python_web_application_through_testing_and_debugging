import json
from flask import Flask,render_template,request,redirect,flash,url_for
from utils import loadClubs, loadCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def showSummary():
    
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
    print("toto")
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)



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
            return render_template('booking.html', club=club, competition=competition), 400
    else:
        # Update of the number of remaining places for the competition
        selected_competition['numberOfPlaces'] = int(selected_competition['numberOfPlaces']) - places_required 
        
        # Updating the number of points remaining for a club
        club['points'] = int(club['points']) - places_required
        
        # Adding a notification message to the user session
        flash('booking complete')
        
        # Home page display
        return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))