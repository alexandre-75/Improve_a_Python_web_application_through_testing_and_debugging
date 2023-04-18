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
        email_club = list[0]
        return render_template('welcome.html', club=email_club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))