import server
from server import app


class TestPointsAllowed:

    client = app.test_client()

    competition = [
        {
            "name": "TestCo",
            "date": "2023-04-17 00:00:00",
            "numberOfPlaces": "100"
        }
    ]

    club = [
        {
            "name": "TestCl",
            "email": "test@example.com",
            "points": 10
        }
    ]

    def setup_method(self):
        
        """
        Set up the test by initializing the competitions and clubs lists with test data.
        """
        
        server.competitions = self.competition
        server.clubs = self.club

    def test_points_within_allowed(self):
        
        """
        Test that a club can purchase places within the allowed number of points.
        """

        self.client.post("/purchasePlaces", data={"places": 5, "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
        assert int(self.club[0]["points"]) >= 0

    def test_more_points_than_allowed(self):
        
        """
        Test that a club cannot purchase more places than the number of points they have.
        """
        response = self.client.post("/purchasePlaces", data={"places": 70, "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
    
        assert response.status_code == 400

    
    def test_invalid_club_name(self):
        
        """
        Test that a club with an invalid name cannot purchase places.
        """
        
        self.client.post("/purchasePlaces", data={"places": 5, "club": "InvalidClubName", "competition": self.competition[0]["name"]})
        assert int(self.club[0]["points"]) == 0

    def test_invalid_competition_name(self):
        
        """
        Test that a club cannot purchase places for an invalid competition name.
        """
        
        self.client.post("/purchasePlaces", data={"places": 5, "club": self.club[0]["name"], "competition": "InvalidCompetitionName"})
        assert int(self.club[0]["points"]) == 0

    def test_invalid_places_value(self):
        
        """
        Test that a club cannot purchase an invalid number of places.
        """
        
        self.client.post("/purchasePlaces", data={"places": "invalid_places", "club": self.club[0]["name"], "competition": self.competition[0]["name"]})
        assert int(self.club[0]["points"]) == 0
  