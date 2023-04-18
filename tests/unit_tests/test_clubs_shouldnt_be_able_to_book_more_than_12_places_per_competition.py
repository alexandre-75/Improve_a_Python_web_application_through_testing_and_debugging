import server
from server import app


class TestMoreThanTwelvePoints:
    client = app.test_client()
    competition = [
        {
            "name": "TestCo",
            "date": "2023-04-18 18:00:00",
            "numberOfPlaces": "25"
        }
    ]

    club = [
        {
            "name": "TestCl",
            "email": "test@example.com",
            "points": "10"
        }
    ]

    places_booked = [
        {
            "competition": "Test",
            "booked": [5, "Test club"]
        }
    ]

    def setup_method(self):
        server.competitions = self.competition
        server.clubs = self.club
        server.places_booked = self.places_booked

    def test_less_than_twelve(self):
        
        """this test verifies that when a club reserves less than 12 places for a competition,
        the HTTP request returns a 200 OK status code."""
        
        booked = 5
        result = self.client.post("/purchasePlaces",data={"places": booked, "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
        assert result.status_code == 200


    def test_more_than_twelve_once(self):
        
        """this test verifies that when a club reserves more than 12 places for a competition,
        the HTTP request returns a 200 OK status code."""
        
        booked = 13
        result = self.client.post("/purchasePlaces", data={"places": booked, "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
        assert result.status_code == 200
        

    def test_more_than_twelve_added(self):
        
        """this test verifies that when a club reserves more than 12 places for a competition, but in several times,
        the HTTP request returns a 200 OK status code."""
        
        booked = 8
        result = self.client.post("/purchasePlaces", data={"places": booked, "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
        assert result.status_code == 200

 
    def test_competition_does_not_exist(self):
        
        """This test verifies that when a club tries to reserve places for a competition that does not exist,
        the HTTP request returns a 500 Internal Server Error status code."""
    
        booked = 5
        result = self.client.post("/purchasePlaces", data={"places": booked, "club": self.club[0]["name"], "competition": "NonexistentCompetition"})
        assert result.status_code == 500


    def test_club_does_not_exist(self):
        
        """This test verifies that when a nonexistent club tries to reserve places for a competition,
        the HTTP request returns a 500 Internal Server Error status code."""
    
        booked = 5
        result = self.client.post("/purchasePlaces", data={"places": booked, "club": "NonexistentClub", "competition": self.competition[0]["name"]})
        assert result.status_code == 500


    def test_already_booked(self):
        
        """This test verifies that when a club tries to reserve places for a competition that they have already booked for,
        the HTTP request returns a 200 OK status code for the first booking, and 200 OK status code for the second booking"""
    
        booked = 5
        result = self.client.post("/purchasePlaces", data={"places": booked, "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
        assert result.status_code == 200
        
        result = self.client.post("/purchasePlaces", data={"places": booked, "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
        assert result.status_code == 200
 